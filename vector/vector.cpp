#include "vector.h"

#include <iostream>
#include <string>

using namespace std;

struct Foo {
    string name;

    // default constructor
    Foo() : name("") { };
    // parameterized constructor
    Foo(string input) : name(std::move(input)) { };
};

// overloaded ostream operator for cout Foo output
ostream& operator<<(ostream &out, const Foo &foo)
{
    out << foo.name;
    return out;
}

void vector_test()
{
    Foo foo_empty("empty");
    Foo foo_jeff("jeff");
    Foo foo_jay("jay");
    Foo foo_fourth("fourth");

    cout << "foo_empty = " << foo_empty << endl;
    cout << "foo_jeff = " << foo_jeff << endl;

    Vector<Foo> v;
    // causes first array to get initialized
    v.push_back(foo_jay);
    // causes reallocation since size == capacity
    v.push_back(foo_empty);
    // no reallocation
    v.push_back(foo_jeff);
    v.push_back(foo_fourth);
    cout << v << endl;

    // testing pop_back
    v.pop_back();
    cout << v << endl;

    // testing destructor
    {
        Vector<Foo> v_int;
        Foo destructor_test("lol");
        v_int.push_back(destructor_test);
    }

    // testing copy constructor
    Vector<Foo> v_copy(v);
    cout << "v_copy = " << v_copy << endl;
}