/**
 * @file foo.h
 * @author jaysc
 *
 * complex data type
 */

#ifndef C_PRACTICE_FOO_FOO_H
#define C_PRACTICE_FOO_FOO_H

#pragma once

#include <iostream>
#include <string>
using namespace std;

struct Foo {
    string name;

    // default constructor
    Foo() : name("") { };
    // parameterized constructor
    Foo(string input) : name(std::move(input)) { };

    // overloaded ostream operator for cout Foo output
    friend ostream& operator<<(ostream &out, const Foo &foo)
    {
        out << foo.name;
        return out;
    }
};

#endif //C_PRACTICE_FOO_FOO_H
