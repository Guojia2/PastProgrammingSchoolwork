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
#include <time.h>

// Inserts a reminder for a specific day

void insert_to_calendar(int day, const char *value)
{
    if (day >= 1 && day <= 31)
    {
        //printf("test point 3\n");
        addNode(&month.reminders[day - 1], value);

        month.hasReminder[day - 1] = true;
    }
    else
    {
        printf("Invalid day. Please enter a day between 1 and %d.\n", month.month_days);
    }
}

// Reads argv and assumes argc => 3. Parses the input and inserts reminder to calendar
int read_reminder(int argc, char *argv[])
{

    int day = atoi(argv[2]);
   // printf("test point 2\n");

    char *task = (char *)malloc(1024 * sizeof(char)); // Allocate memory for task
    if (task == NULL)
    {
        // Handle memory allocation failure
        perror("Memory allocation failed");
        return 1;
    }
    task[0] = '\0'; // Initialize the task string as empty

    for (int i = 3; i < argc; i++)
    {                          // Start from the 3rd argument
        strcat(task, argv[i]); // Append each argument
        if (i < argc - 1)
        {
            strcat(task, " "); // Add a space between words
        }
    }


   // printf("test point 3\n");

    insert_to_calendar(day, task);
   // printf("test \n");
    free(task);
    return day; // Return the day number
}

// Prints the calendar for the month and indicates days with reminders

void print_calendar()
{

    printf("\n");
    printf("  Sun   Mon   Tue  Wed   Thu   Fri   Sat\n");

    int current_day = 1; // this variable is never used in the program but im keeping it here in case i neeed it later
    int start_day = month.start_day;

    // prints the blank space in the first row of the month calendar
    for (int i = 0; i < start_day; i++)
    {
        printf("      ");
    }

    for (int i = 1; i <= month.month_days; i++)
    {
        if (month.reminders[i - 1])
        {
            printf(" (%2d) ", i); // Mark days with reminders
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
    print_reminders();
    printf("\n");

    // prints a horizontal line so program output is more readable.
    for (int i = 0; i < 20; i++)
    {
        printf("=");
    }
    printf("\n");
    printf("\n");
}

Month initializeMonth(void)
{
    time_t now = time(NULL);
    struct tm *t = localtime(&now);
    month.month_idx = t->tm_mon + 1; // i added +1 here because i am turning month_idx into an enum
    t->tm_mday = 1;
    mktime(t);
    month.start_day = t->tm_wday;
    month.month_days = t->tm_mday;
    while (t->tm_mon == month.month_idx - 1)
    {
        month.month_days = t->tm_mday;
        t->tm_mday++;
        mktime(t);
    }
    for (int i = 0; i < 31; i++)
    {
        month.reminders[i] = NULL; // Initialize each day’s reminder as NULL
    }

    return month;
}

void print_reminders()
{

    const char *daysOfWeek[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};

    printf("\n%s Reminders:\n", getMonthName(month.month_idx));
    for (int i = 0; i < month.month_days; i++)
    {
        if (month.hasReminder[i])
        {
            int day_of_week = (month.start_day + i) % 7; // Calculate day of the week

            printf("%s %2d: ", daysOfWeek[day_of_week], i + 1); // Print day of the week and date
            printList(month.reminders[i]);
            // printf("\n");
        }
    }
}

void freeMonth(Month month)
{
    int i = 0;
    for (i = 0; i < 31; i++)
    {
        freeList(month.reminders[i]);
    }
}

void removeReminder(int day, const char *value)
{

    deleteNode(month.reminders[day], value);
}
void printToday()
{

    time_t t = time(NULL);
    // Convert it to local time
    struct tm *tm_info = localtime(&t);
    // Get the current day of the month
    int dayOfMonth = tm_info->tm_mday;

    const char *daysOfWeek[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};

    int day_of_week = (month.start_day + dayOfMonth - 1) % 7; // Calculate day of the week
    printf("%s %2d: ", daysOfWeek[day_of_week], dayOfMonth); // Print day of the week and date
    printList(month.reminders[dayOfMonth - 1]);

    return;
}

const char *getMonthName(enum MonthEnum monthId)
{
    switch (monthId)
    {
    case January:
        return "January";
    case February:
        return "February";
    case March:
        return "March";
    case April:
        return "April";
    case May:
        return "May";
    case June:
        return "June";
    case July:
        return "July";
    case August:
        return "August";
    case September:
        return "September";
    case October:
        return "October";
    case November:
        return "November";
    case December:
        return "December";
    default:
        return "Unknown";
    }
}
