/*The implementation file containing functions for inserting reminders into the calendar
and displaying the calendar.

tasks:
1. Display the calendar
    - calendar must display the month of November as in lab 3.
    - All days with reminders on them should be shown as d
2. Insert reminders into the calendar
    - the <reminder.h> header gives us a struct of type month that we can use
    - reminder.h also declares functions but does not define them.

*/

#include "reminder.h"
#include <stdio.h>
#include <string.h>

// Inserts a reminder for a specific day
void insert_to_calendar(int day, const char *value)
{
    if (day >= 1 && day <= 30)
    {
        strcpy(November.reminder_str[day - 1], value);
        November.reminders[day - 1] = true;
    }
    else
    {
        printf("Invalid day. Please enter a day between 1 and 30.\n");
    }
}

// Reads a reminder from the user and returns the day number
int read_reminder(char *str, int n)
{
    int day;
    char task[90]; // For the task part of the user input (assumes task length won't exceed 89 characters)

    printf("Enter day and reminder (0 to quit): ");

    // Read the input from the user
    if (fgets(str, n, stdin) == NULL)
    {
        return 0; // Return 0 if reading fails
    }

    // check if the user entered 0 to quit
    if (atoi(str) == 0)
    {
        return 0; // Quit if day is 0
    }

    // Extract day and task using sscanf
    sscanf(str, "%d %[^\n]", &day, task);

    insert_to_calendar(day, task);

    return day; // Return the day number
}

// Prints the calendar for November and indicates days with reminders
void print_calendar()
{
    printf("\n");
    printf("  Sun   Mon   Tue  Wed   Thu   Fri   Sat\n");

    int current_day = 1;
    int start_day = November.start_day;

    // prints the blank space in the first row of the month calendar
    for (int i = 0; i < start_day; i++)
    {
        printf("      "); 
    }

    for (int i = 1; i <= November.month_days; i++)
    {
        if (November.reminders[i - 1])
        {
            printf(" (%d) ", i); // Mark days with reminders
        }
        else
        {
            printf(" %3d  ", i);
        }

        if ((i + start_day) % 7 == 0)
        {
            printf("\n");
        }
    }
    printf("\n");

    // Print reminders for each day
    printf("\nReminders:\n");
    for (int i = 0; i < 30; i++)
    {
        if (November.reminders[i])
        {
            printf("Day %d: %s\n", i + 1, November.reminder_str[i]);
        }
    }



    printf( "\n");
    // prints a horizontal line so program output is more readable.
    for (int i = 0; i < 20; i++){
        printf("=");
    }
    printf( "\n");
    printf( "\n");

}
