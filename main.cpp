#include "last-k-lines.h"
#include "reverse-string.h"
#include "vector-implementation.h"

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

int main()
{
//    last_k_lines("test.txt", 10);
//    std::cout << std::endl;
//    last_k_lines("test.txt", 2);

//    char s1[] = "string";
//    char s2[] = "test";
//    char s3[] = "";   // empty string
//
//    reverse_string(s1);
//    reverse_string(s2);
//    reverse_string(s3);
//    reverse_string(NULL); // test invalid input

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


    return 0;
}