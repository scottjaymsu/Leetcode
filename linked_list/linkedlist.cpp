/**
 * @file linkedlist.cpp
 * @author jaysc
 */

#include "linkedlist.h"
#include <iostream>
using namespace std;

ostream& operator<<(ostream& out, Node const& node)
{
    out << node.data;
    return out;
}

// print linked list
void LinkedList::print()
{
    // init at head
    Node *temp = head;
    cout << "linked list = ";
    while (temp != nullptr)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

// insert node at head of linked list
void LinkedList::insert_head(int data)
{
    Node *node = new Node(data);
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
void LinkedList::remove_head()
{
    // edge case : empty list
    if (head == nullptr)
    {
        cout << "No nodes to remove!" << endl;
        return;
    }
    Node *temp = head;
    head = head->next;
    delete temp;
}

void linked_test()
{
    // test node constructor
    Node one(1);
    cout << one << endl;

    // init linked list
    LinkedList list = LinkedList();

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
}
