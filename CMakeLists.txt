cmake_minimum_required(VERSION 3.27)
project(c_practice)

set(CMAKE_CXX_STANDARD 14)

add_executable(c_practice
        last-k-lines.cpp
        main.cpp
        last-k-lines.h
        reverse-string.cpp
        reverse-string.h
        vector-implementation.h
)

# Copy test.txt into the build directory so the program can find it
configure_file(${CMAKE_SOURCE_DIR}/test.txt
        ${CMAKE_BINARY_DIR}/test.txt
        COPYONLY)