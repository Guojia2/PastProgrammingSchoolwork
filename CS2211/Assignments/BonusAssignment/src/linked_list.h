#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <stddef.h> // For NULL
#include <stdbool.h>


// Define the structure for a node in the linked list
typedef struct Node {
    char* data;           // Pointer to a string (im pretty sure its dynamically allocated)
    struct Node* next;
} Node;

// Function prototypes
Node* addNode(Node** head, const char* value); // Adds a node with a string
Node* deleteNode(Node* head, const char* value); // Deletes the first node with the given string
Node* deleteNodeByIndex(Node* head, int index); // Deletes node by index. This method uses 1-indexing.
void freeList(Node* head);                       // Frees all nodes in the list
void printList(Node* head);                     // Prints all strings in the list
void printNode(Node* node);
bool isEmpty(Node* head);// i may not need this function after all



#endif // LINKED_LIST_H
