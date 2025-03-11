#include "person.h"
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include "interact.h"
#include <signal.h>  
#include <stdlib.h>

void printMenu(void)
{
    printf("\n");
    printf("_______________________\n");
    printf("\nMenu:\n");
    printf("\n");
    printf("1. Add a person\n");
    printf("2. Update a person\n");
    printf("3. Print all people\n");
    printf("4. Delete a person\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
}

bool isValidFloat(const char *str)
{
    int dotCount = 0;

    // Check each character in the input string
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == '.')
        {
            dotCount++;
            if (dotCount > 1)
            { // More than one decimal point is invalid
                return false;
            }
        }
        else if (!isdigit(str[i]) && (i != 0 || str[i] != '-'))
        {
            return false; // Non-digit character (and not the initial '-' sign)
        }
    }

    return true; // Valid number
}

void readName(char *name)
{
    getchar(); // Clear newline from previous input
    fgets(name, MAX_NAME_LENGTH, stdin);

    // Trim leading spaces
    int start = 0;
    while (isspace(name[start]))
    {
        start++;
    }

    // Copy the trimmed name to the beginning of the array
    memmove(name, name + start, strlen(name) - start + 1);

    // Remove trailing newline character
    name[strcspn(name, "\n")] = '\0';
}

bool containsDigit(const char *str)
{
    int length = strlen(str); // Get the length of the string
    for (int i = 0; i < length; i++)
    { // Loop through each character by index
        if (isdigit((unsigned char)str[i]))
        {
            return true; // Return true if a digit is found
        }
    }
    return false; // Return false if no digits are found
}

Choice getChoice(void)
{
    int choice;
    if (scanf("%d", &choice) != 1 || choice < 1 || choice > 5)
    {
        while (getchar() != '\n')
            ;           // clear invalid input
        return INVALID; // invald choice
    }
    return (Choice)(choice - 1); // adjust for enum indexing
}

RoleType getRole(void)
{

    RoleType roleInput;
    printf("Enter role (0 for Student, 1 for Professor): ");

    while (scanf("%d", &roleInput) != 1 || (roleInput != STUDENT && roleInput != PROFESSOR))
    {
        printf("Invalid role type. Please enter 0 for Student or 1 for Professor.\n");
        while (getchar() != '\n')
            ; // Clear invalid input

        printf("Enter role (0 for Student, 1 for Professor): ");
    }

    return roleInput;
}
int getID(RoleType roleIn)
{
    int id;
    if (roleIn == STUDENT)
    {
        do
        {
            printf("Enter Student ID: ");

            int result = scanf("%d", &id);

            // scanf will return 1 if it reads an integer, so we can check whether the user inputted an integer this way
            if (result != 1)
            {
                printf("Invalid ID. ID must be a postitive number. \n");
            }
            // checks if user inputted an id that is a postive number
            else if (id <= 0)
            {
                printf("Invalid ID. ID must be a positive number. \n");
            }
            else
            {
                break;
            }

        } while (true);
    }

    else if (roleIn == PROFESSOR)
    {
        do
        {
            printf("Enter Professor ID: ");

            int result = scanf("%d", &id);

            // scanf will return 1 if it reads an integer, so we can check whether the user inputted an integer this way
            if (result != 1)
            {
                printf("Invalid ID. ID must be a postitive number. \n");
            }
            // checks if user inputted an id that is a postive number
            else if (id <= 0)
            {
                printf("Invalid ID. ID must be a positive number. \n");
            }
            else
            {
                break;
            }

        } while (true);
    }
    return 0;
}

char *getName(void)
{
    char *name = malloc(MAX_NAME_LENGTH * sizeof(char));
    do
    {
        printf("Enter name: ");
        readName(name);
        if (containsDigit(name))
        {
            printf("Invalid name. Name cannot contain numbers \n");
        }
        else
        {
            return name;
        }

    } while (true);

    return name;
}

float getInfo(RoleType roleIn)
{
    if (roleIn == STUDENT)
    {
        float gpa;

        printf("Enter GPA: ");
        while (scanf("%f", &gpa) != 1)
        {
            printf("Invalid GPA. GPA must be a positive number. \n");
            printf("Enter GPA: ");
        }
        return gpa;
    }

    else if (roleIn == PROFESSOR)
    {
        float salary;
        printf("Enter salary: ");
        while (scanf("%f", &salary) != 1)
        {
            printf("Invalid salary. Salary must be a positive number (slavery is illegal). \n");
            printf("Enter salary: ");
        }
        return salary;
    }
    return 0;
}




// Signal handler for SIGINT (Ctrl+C)
void handle_sigint(int sig) {
    printf("\nCaught signal SIGINT (Ctrl+C). Gracefully exiting...\n");
    // Perform cleanup (e.g., free memory)
    freeAll(head);  
    exit(0);  // Exit 
}

// Signal handler for SIGTERM (termination signal)
void handle_sigterm(int sig) {
    printf("\nCaught signal SIGTERM. Exiting gracefully...\n");
    // Perform cleanup (e.g., free memory)
    freeAll(head);  
    exit(0);  // Exit gracefully
}

// Set up the signal handlers
void setup_signal_handlers() {
    signal(SIGINT, handle_sigint);
    signal(SIGTERM, handle_sigterm);
}


