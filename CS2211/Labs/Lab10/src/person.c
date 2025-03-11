#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include "interact.h"
#include "linked_list.h"
#include <stdlib.h>

void deletePerson(Node **head)
{

    char *targetName = getName();
    RoleType role = getRole();
    int id = getID(role);

    deleteNode(*head, targetName, id, role);
}
void addPerson(Node **head)
{
    // Get the user inputs
    RoleType role = getRole();         // Function to get the role (STUDENT or PROFESSOR)
    char *targetName = getName();      // Function to get the person's name

    int id = getID(role);              // Function to get ID, depends on role
    float info = getInfo(role);

    
    // Initialize the Person structure
    Person person = {};
 
    person.role = role;                // Set the role (STUDENT or PROFESSOR)

    // Conditionally set the info field based on role
    if (role == STUDENT) {
        // Initialize the StudentInfo part of the union
        person.info.student.StudentId = id; // Set the student ID
        person.info.student.GPA = info;     // Set the GPA 
    } else if (role == PROFESSOR) {
        // Initialize the ProfessorInfo part of the union
        person.info.professor.ProfessorId = id; // Set the professor ID
        person.info.professor.salary = info;  // Set the salary
    }

    strcpy(person.name, targetName);   // Copy the name into the Person's name field

    // Add the person to the linked list
    addNode(*head, person);

    printf("Person added successfully");

    free(targetName);
    return;
}


void updatePerson(Node **head)
{


    
}