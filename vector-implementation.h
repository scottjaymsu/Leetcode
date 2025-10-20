/**
 * @file vector-implementation.h
 * @author jaysc
 *
 *
 */

#ifndef C_PRACTICE__VECTOR_IMPLEMENTATION_H
#define C_PRACTICE__VECTOR_IMPLEMENTATION_H

#include <cstdlib>

using namespace std;

// template class for generic types
template <typename T>
class Vector {
private:
    // number of elements
    int size = 0;
    // max elements allowed
    int capacity = 0;
    // array underlying structure
    T *arr = nullptr;

public:
    // Default constructor
    Vector(){};
    // Assignment constructor
//    Vector& operator=(const Vector& other);
    // Add elements to vector
    void push_back(const T& element)
    {
       // first element pushed
       if (arr == nullptr)
       {
           capacity = 1;
           arr = (T *) malloc(capacity * sizeof(T));
       }

       //

        // construct new element at arr[size] using placement new
        // placement new only constructs not allocate
        // new(address) Type(args)
        new(&arr[size]) T(element);
        size++;
    }

    // Remove elements from vector
//    T pop();
};

#endif //C_PRACTICE__VECTOR_IMPLEMENTATION_H