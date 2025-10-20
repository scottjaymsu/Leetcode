// write a method to print the last k lines of an input file 
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

/**
 * prints last k lines
 * @param file_name - file input
 * @param k - number of lines to print
 */
void last_k_lines(char file_name[], int k)
{
    // read in filestream
    std::ifstream file(file_name);
    // ensure the file is open
    if (!file.is_open())
    {
        std::cerr << "Error opening file: " << file_name << std::endl;
        return;
    }

    // circular array (buffer) to hold last k lines
    string buffer[k];
    int size = 0;

    // peek at next char to not count EOF as line from file
    while (file.peek() != EOF)
    {
        // getline from file and store in buffer
        std::getline(file, buffer[size % k]);
        ++size;
    }

    // print starting from correct location in buffer
    // if there were more than k values added,
    // then calculate the starting idx similar to how they were stored
    int start = size > k ? (size % k) : 0;
    // number of lines in buffer - will not go over k nums
    int count = std::min(k, size);

    // print values
    for (int i = 0; i < count; ++i)
    {
        std::cout << buffer[(start + i) % k] << std::endl;
    }
}