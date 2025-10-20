/**
 * @file vector.h
 * @author jaysc
 *
 *
 */

#ifndef C_PRACTICE__VECTOR_IMPLEMENTATION_H
#define C_PRACTICE__VECTOR_IMPLEMENTATION_H

#include <cstdlib>
#include <iostream>

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

    // Destructor
    ~Vector()
    {
        for (int i = 0; i < size; ++i)
        {
            // deallocate template variables to clean up memory leaks
            arr[i].~T();
        }
        // deallocate array itself
        free(arr);
    }

    // Copy constructor
    Vector(Vector<T> const &other)
    {
        capacity = other.capacity;
        size = other.size;

        if (size <= 0)
        {
            arr = nullptr;
            return;
        }

        // raw allocation for array
        arr = (T *) malloc(capacity * sizeof(T));
        // allocate templated elements from other array
        for (int i = 0; i < size; ++i)
        {
            // new(address) Type(args)
            new (&arr[i]) T(other.arr[i]);
        }
    }

    // Add elements to vector
    void push_back(const T& element)
    {
       // first element pushed
       if (arr == nullptr)
       {
           capacity = 1;
           arr = (T *) malloc(capacity * sizeof(T));
       }

       // full vector -> reallocation via array doubling
       if (size >= capacity)
       {
           capacity *= 2;
           T *temp = (T *) malloc(capacity * sizeof(T));

           // copy old array
           for (int i = 0; i < size; ++i)
           {
               // placement new
               new (&temp[i]) T(arr[i]);
           }

           // free old array
           for (int i = 0; i < size; ++i)
           {
               // deallocate each template object
               // in case object manages its own memory
               // avoids memory leaks for internal buffers when array is freed
               arr[i].~T();
           }
           free(arr);
           arr = temp;
       }

       // construct new element at arr[size] using placement new
       // placement new only constructs not allocate
       // new(address) Type(args)
       new(&arr[size]) T(element);
       size++;
    }

    // remove last element in array
    void pop_back()
    {
        // edge case : empty vector
        if (!size) return;

        // deallocate last element and move size back one
        arr[--size].~T();
    }

    // overloaded operator for testing
    template<typename U>
    friend ostream& operator<<(ostream& out, Vector<U> const& v);
};

template<typename U>
ostream& operator<<(ostream& out, Vector<U> const& v)
{
    out << "[ ";

    for (int i = 0; i < v.size; ++i)
    {
        out << v.arr[i] << " ";
    }

    out << "]";

    return out;
}

void vector_test();

#endif //C_PRACTICE__VECTOR_IMPLEMENTATION_H