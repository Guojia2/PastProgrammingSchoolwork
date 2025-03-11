#include "reminder.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Declare November as a global variable
struct Month November = {.month_days = 31, .start_day = 1};

int main()
{

    // Initialize reminder flags to false and reminder strings to empty
    for (int i = 0; i < 30; i++)
    {
        November.reminders[i] = false;
        strcpy(November.reminder_str[i], "");
    }
    bool running = true;
    while (running)
    {
        char input[100];
        int day;
        // Call read_reminder and check the return value
        day = read_reminder(input, sizeof(input));
        
        // If the user entered 0, quit the program
        if (day == 0)
        {
            return 0;
        }

        print_calendar();
    }
}
