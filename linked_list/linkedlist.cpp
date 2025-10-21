/**
 * @file linkedlist.cpp
 * @author jaysc
 */

#pragma once

#include "linkedlist.h"
#include "../foo/foo.h"
#include <iostream>
using namespace std;

template <typename T>
ostream& operator<<(ostream& out, Node<T> const& node)
{
    out << node.data;
    return out;
}

template <typename T>
LinkedList<T>::~LinkedList()
{
    Node<T> *current = head;
    // free all nodes
    while (current != nullptr)
    {
        Node<T> *next = current->next;
        delete current;
        current = next;
    }
}

// print linked list
template <typename T>
void LinkedList<T>::print()
{
    // init at head
    Node<T> *temp = head;
    cout << "linked list = ";
    while (temp != nullptr)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

// insert node at head of linked list
template <typename T>
void LinkedList<T>::insert_head(T data)
{
    Node<T> *node = new Node<T>(data);
    // edge case : empty linked list
    if (head == nullptr)
    {
        head = node;
        return;
    }

    node->next = head;
    head = node;
}

// remove node at head
template <typename T>
void LinkedList<T>::remove_head()
{
    // edge case : empty list
    if (head == nullptr)
    {
        cout << "No nodes to remove!" << endl;
        return;
    }
    Node<T> *temp = head;
    head = head->next;
    delete temp;
}

void linked_test()
{
    // test node constructor
    Node<int> one(1);
    cout << one << endl;

    // init linked list
    LinkedList<int> list = LinkedList<int>();

    // insert into empty linked list
    list.insert_head(2);
    list.print();
    // insert into partially linked list with nodes
    list.insert_head(1);
    list.print();

    // remove head
    list.remove_head();
    list.print();
    list.remove_head();
    list.print();
    // remove head on empty linked list
    list.remove_head();

    // testing with complex type <Foo>
    Foo foo(string("jay"));
    LinkedList<Foo> list_two = LinkedList<Foo>();
    list_two.insert_head(foo);
    list_two.print();
    list_two.remove_head();
    list_two.print();

    // testing destructor
    {
        Foo foo_two(string("jeff"));
        LinkedList<Foo> list_three = LinkedList<Foo>();
        list_three.insert_head(foo_two);
    }

}
