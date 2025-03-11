#include "linked_list.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "reminder.h"

// Adds a new node with the given string to the end of the list
Node *addNode(Node **head, const char *value)
{
    Node *newNode = (Node*)malloc(sizeof(Node)); // newNode should now point to a block of memory allocated for a Node

    // if newNode is a null pointer, that means malloc failed
    if (!newNode)
    {
        fprintf(stderr, "Memory allocation failed.\n");
        return *head;
    }
    newNode->data = strdup(value); // Duplicate the string for storage
    newNode->next = NULL;

    if (*head == NULL)
    { // If the list is empty, the new node is the head
        *head = newNode;
    }
    else
    {
        // Traverse to the end of the list and append the new node
        Node *current = *head;
        while (current->next)
        {
            current = current->next;
        }
        current->next = newNode;
    }

    return *head;
}

// Deletes the first node with the given string
Node *deleteNode(Node *head, const char *value)
{
    if (!head)
    {
        return NULL; // List is empty
    }

    // If the head node contains the string
    if (strcmp(head->data, value) == 0)
    {
        Node *temp = head;
        head = head->next;
        free(temp->data); // Free the string
        free(temp);       // Free the node
        return head;
    }

    Node *current = head;
    while (current->next && strcmp(current->next->data, value) != 0)
    {
        current = current->next;
    }

    // If a node with the string is found
    if (current->next)
    {
        Node *temp = current->next;
        current->next = temp->next;
        free(temp->data); // Free the string
        free(temp);       // Free the node
    }

    return head;
}

// Frees all nodes in the list
void freeList(Node *head)
{
    Node *current = head;
    while (current)
    {
        Node *temp = current;
        current = current->next;
        free(temp->data); // Free the string
        free(temp);       // Free the node
    }
}

// prints all strings in the list.
void printList(Node *head)
{

    Node *current = head;
    int reminderCount = 1;
    while (current)
    {   

        if (reminderCount == 1)
        {
            printf("(%d) ", reminderCount);
        }
        else
        {
            printf("        (%d) ", reminderCount);
        }
        
        
        
        printNode(current);
        printf("\n");
        reminderCount++;
        current = current->next;
    }
    
}

// this function will be used when we print reminders
void printNode(Node *node)
{

    if (!node)
    {

        printf("Node is NULL \n");
    }

    if (node)
    {
        printf("%s ",node->data);
    }

    return;
}
