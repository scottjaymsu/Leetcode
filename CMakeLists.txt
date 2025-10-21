cmake_minimum_required(VERSION 3.27)
project(c_practice)

set(CMAKE_CXX_STANDARD 14)

add_executable(c_practice
        k_lines/last-k-lines.cpp
        vector/vector.cpp
        k_lines/last-k-lines.h
        reverse_string/reverse-string.cpp
        reverse_string/reverse-string.h
        vector/vector.h
        main.cpp
        linked_list/linkedlist.h
        linked_list/linkedlist.cpp
)

# Copy test.txt into the build directory so the program can find it
configure_file(${CMAKE_SOURCE_DIR}/k_lines/test.txt
        ${CMAKE_BINARY_DIR}/k_lines/test.txt
        COPYONLY)