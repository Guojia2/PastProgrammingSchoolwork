#include <stdio.h>
#include "interact.h"
#include "reminder.h"
#include <stdlib.h>
#include "linked_list.h"
#include <signal.h>
#include <ctype.h>

Month month;

// Signal handler for SIGINT (Ctrl+C)
void handle_sigint(int sig)
{
    printf("\nProgram interrupted...\n");
    // Perform cleanup
    printf("Writing to file... \n");
    writingToFile("reminder.txt", month.reminders);
    printf("Reminders saved. Now exiting.\n");
    freeMonth(month);
    // flushBuffer();

    exit(0); // Exit
}

// Signal handler for SIGTERM (termination signal)
void handle_sigterm(int sig)
{
    printf("\nProgram terminated...\n");
    // Perform cleanup
    printf("Writing to file... \n");
    writingToFile("reminder.txt", month.reminders);
    printf("Reminders saved. Now exiting.\n");
    freeMonth(month);
    exit(0); // Exit gracefully
}

// Set up the signal handlers
void setup_signal_handlers()
{
    signal(SIGINT, handle_sigint);
    signal(SIGTERM, handle_sigterm);
}

int main(int argc, char *argv[])
{

    // initializes month, reads any preexisitng reminders
    month = initializeMonth();
    readingFromFile("reminder.txt", month.reminders);
    setup_signal_handlers();

    char usage[] = "Usage: /gcal [view | add ‹day> ‹reminder> | remove ‹day> <index> | today] \n";
    if (argc < 2 )
    {
        printf("Invalid arguments\n");
        printf("%s", usage);
        return 0;
    }


    char *command = argv[1];
    // switches cases based on the command entered by the user
    if (strcmp(command, "view") == 0)
    {
        printf("Viewing reminders...\n");
        print_calendar();
    }

    else if (strcmp(command, "add") == 0)
    {
        if (argc < 4)
        {
            printf("Usage: gcal add <day> <reminder>\n");
            return 1;
        }
        //int day = atoi(argv[2]);  // Convert day to integer
        
  
        //printf("argc is %d\n", argc);
        //printf("test point 1\n");
        read_reminder(argc, argv);
        if (isdigit(*argv[2]))
        {
            print_calendar();
        }
        
        
    }

    else if (strcmp(command, "remove") == 0)
    {
        if (argc < 4)
        {   
            printf("Invalid arguments.\n");
            printf("Usage: gcal remove <day> <index>\n");
            return 1;
        }
        int day = atoi(argv[2]);
        int index = atoi(argv[3]);
        //printf("Removing reminder %d from day %d...\n", index, day);
        if (month.reminders[day - 1] != NULL)
        {   
            // printf("day is %d\n", day);
            // printf("index is %d\n", index);
            month.reminders[day-1] = deleteNodeByIndex(month.reminders[day - 1], index);
            if (!month.reminders[day - 1]){
                month.hasReminder[day - 1] = false;
            }
            print_calendar();
        }
        else
        {
            printf("No reminders found for day %d\n", day);
        }
    }

    else if (strcmp(command, "today") == 0)
    {
        printf("Showing today's reminders...\n");
        printToday();
    }
    else
    {
        printf("Invalid command: %s\n", command);
        printf("Usage: /gcal [view | add <day> <reminder> | remove <day> <index> | today]\n");
        printf("default");
        return 1;
    }

   //printf("Savings reminders... \n");
    writingToFile("reminder.txt", month.reminders);
    //printf("Reminders saved. Now exiting.\n");
    freeMonth(month);

    return 0;
}