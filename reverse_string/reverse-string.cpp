/**
 * @file reverse-string.cpp
 * @author jaysc
 */

#include <iostream>

using namespace std;

// implement a function which reverses a null-terminated string
// assuming we don't know size
void reverse_string(char *str)
{
    // edge case : invalid string
    if (str == NULL)
    {
        std::cout << "Cannot reverse invalid string input" << std::endl;
        return;
    }

    // iterate until null-terminator
    char *end = str;
    while (*end)
    {
        ++end;
    }
    // decrement back from null-terminator
    --end;

    // string front and back characters until they meet in middle
    char* start = str;
    char temp;
    while (start < end)
    {
        temp = *start;
        *start = *end;
        *end = temp;

        ++start;
        --end;
    }

    std::cout << str << std::endl;
    return;
}