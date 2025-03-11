
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include "interact.h"
#include "linked_list.h"
#include "person.h"

// Contains the main function, the program's entry point.


int numPeople = 0;


int main(void)
{

    head = NULL;

    void setup_signal_handlers();
    Choice choice;
    // Main program loop
    while (1)
    {
        printMenu();
        choice = 0;
        choice = getChoice();

        switch (choice)
        {
        case ADD:
            addPerson(&head);
            break;
        case UPDATE:
            updatePerson(&head);
            break;
        case PRINT:

            printList(head);

            break;
        case DELETE:
            deletePerson(&head);
            break;
        case EXIT:
            printf("Exiting program.\n");
            return 0;
        default:
            printf("Invalid choice. Please try again.\n");
        }
    }
    return 0;
}
