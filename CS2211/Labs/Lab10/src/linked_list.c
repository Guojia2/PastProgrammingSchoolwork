
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "person.h"
#include "interact.h"

#include "linked_list.h"


Node *head = NULL;
// Adds a new node with the given person struct to the end of the list
Node *addNode(Node *head, Person value)
{
    Node *newNode = (Node *)malloc(sizeof(struct Node)); // newNode should now point to a block of memory allocated for a Node

    // if newNode is a null pointer, that means malloc failed
    if (!newNode)
    {
        fprintf(stderr, "Memory allocation failed.\n");
        return head;
    }
    newNode->person = value;
    newNode->next = NULL;

    if (!head)
    {
        return newNode; // If list is empty, newNode becomes the head
    }

    Node *current = head;
    while (current->next)
    {
        current = current->next;
    }
    current->next = newNode;

    return head;
}



// helper function to find a desired node in the linked list
bool personMatch(Person person1, char *name, int targetID, RoleType targetRole)
{
    if (person1.role != targetRole)
    {
        return false;
    }

    if (person1.role == PROFESSOR)
    {
        return (person1.info.professor.ProfessorId == targetID && strcmp(person1.name, name) == 0);
    }
    else if (person1.role == STUDENT)
    {
        return (person1.info.student.StudentId == targetID && strcmp(person1.name, name) == 0);
    }
    return false;
}

// Deletes the first node with a Person struct that matches the given name,id, and role
Node* deleteNode(Node *head, char *targetName, int targetID, RoleType targetRole)
{
    if (!head)
    {
        printf("Database is empty \n");
        return NULL; // List is empty
    }

    Node *current = head;
    Node *previous = NULL;

    // Iterate through the linked list to find the target node
    while (current)
    {
        if (personMatch(current->person, targetName, targetID, targetRole))
        {
            if (previous == NULL)
            {
                // Case 1: The head node contains the target person
                head = current->next;
            }
            else
            {
                // Case 2 & 3: The node is in the middle or at the end
                previous->next = current->next;
            }

            // Free the memory of the matched node
            free(current->person.name); // Free dynamically allocated memory
            free(current);              // Free the node itself

            printf("Person deleted successfully.\n");
            return head; // Return the updated head
        }
        // Move the pointers forward
        previous = current;
        current = current->next;
    }
    // If we reach here, the target node was not found
    printf("Person was not found.\n");
    return head;
}



// finds a person in the linked list and updates their GPA or salary, depending on the RoleType
void updateNode(Node *head, char *targetName, int targetID, RoleType targetRole)
{
    Node *current = head;
    while (current && !(personMatch(current->person, targetName, targetID, targetRole)))
    {
        current = current->next;
    }

    // at this point in the code, there are 2 cases
    // 1. Current is null
    // 2. current contains the person we want

    //Case 1:
    if (!current)
    {
        printf("Person not found");
        return;
    }

    //Case 2:
    else
    {
        printf("Person has been found succesfully. \n");

        if (targetID == STUDENT)
        {
            printf("Please enter the new GPA: \n");
            scanf("%f", &current->person.info.student.GPA);

            printf("Student information updated succesfully \n");
        }


        else if (targetID == PROFESSOR)
        {
            printf("Please enter the new salary \n"); 
            scanf("%lf", &current->person.info.professor.salary);
            printf("Professor information updated succesfully \n");
        }

    }
    return;
}

// Frees all nodes in the list
void freeAll(Node *head)
{
    Node *current = head;
    while (current)
    {
        Node *temp = current;
        current = current->next;
        free(temp); // Free the node
    }
}

/// prints the entire linked list
void printList(Node *head)
{
    Node *current = head;
    printf("Linked List: ");
    while (current)
    {
        printNode(current);
        printf("\n");
        current = current->next;
    }
    printf("NULL\n");
}

// Prints the details of a node
void printNode(Node *node)
{
    char *name = node->person.name;
    RoleType role = node->person.role;
    int id;
    float GPA;
    double salary;


    char *roleString = NULL;

    if (role == PROFESSOR)
    {
        id = node->person.info.professor.ProfessorId;
        salary = node->person.info.professor.salary;
        roleString = "Professor";  // Assign roleString for professor
    }
    else if (role == STUDENT)
    {
        id = node->person.info.student.StudentId;
        GPA = node->person.info.student.GPA;
        roleString = "Student";  // Assign roleString for student
    }

    // Print the information
    printf("Role: %s\n", roleString);  // Print role
    printf("Name: %s\n", name);        // Print name
    printf("ID: %d\n", id);            // Print ID

    if (role == PROFESSOR)
    {
        printf("Salary: %f\n", salary);  // Print salary for professors
    }
    if (role == STUDENT)
    {
        printf("GPA: %f\n", GPA);  // Print GPA for students
    }
}
