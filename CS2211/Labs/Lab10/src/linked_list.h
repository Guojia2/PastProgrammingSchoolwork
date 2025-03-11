
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <signal.h>
#include "person.h"
#include <stddef.h> // For NULLs
#include <stdbool.h>

//Deﬁnes the Node struct and manages the linked list
//functions to add a note, update a node, remove a node, print the linked list nodes,
//and remove all nodes (to free dynamically allocated memory).

#ifndef LINKED_LIST_H
#define LINKED_LIST_H



// Define the structure for a node in the linked list
typedef struct Node {
    Person person;        
    struct Node* next;
} Node;

extern Node* head;


// Function prototypes
Node *addNode(Node *head, Person value); // Adds a node with a person
Node *deleteNode(Node *head, char *targetName, int targetID, RoleType targetRole); // Deletes the first node with the given person
void freeAll(Node* head);                       // Frees all nodes in the list
void printList(Node* head);                     // Prints all nodes in the list
void printNode(Node* node);                     // prints a single node in the list
bool isEmpty(Node* head);                       // i may not need this function after all
void updateNode(Node* head,char *targetName, int targetID, RoleType targetRole );
bool personMatch(Person person1, char* name, int targetID, RoleType targetRole);



#endif // LINKED_LIST_H

