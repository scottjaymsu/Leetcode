/**
 * @file linkedlist.h
 * @author jaysc
 *
 *
 */

#ifndef C_PRACTICE_LINKED_LIST_LINKEDLIST_H
#define C_PRACTICE_LINKED_LIST_LINKEDLIST_H

/**
 * Goal:
 * Implement insert/delete at head, tail, and middle.
 * Reverse a list in-place.
 */
#include <iostream>
using namespace std;

struct Node {
    int data = NULL;
    Node *next = nullptr;

    // default constructor
    Node(){ }
    // constructor with data input
    Node(int input) : data(input) {}
    // overloaded ostream operator
    ostream& operator<<(ostream& out);
};

class LinkedList {
private:
    Node *head = nullptr;

public:
    // default constructor
    LinkedList() {}
    // print linked list
    void print();
    // insert at head
    void insert_head(int data);
    // remove node at head
    void remove_head();
};

void linked_test();

#endif //C_PRACTICE_LINKED_LIST_LINKEDLIST_H