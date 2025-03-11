#include <stdio.h>
#include "interact.h"
#include "reminder.h"
#include <stdlib.h>
#include "linked_list.h"
#include <signal.h>  


/*

initialize the month;

use readingFromFile(reminders.txt) to read any preexisting reminders on startup;
handle any errors and continue running as normal;

while true:


    printCalendar();

    call read_Reminder() from reminder.h
    printCalendar();


    before exiting, use writeToFIle to write all reminders to reminders.txt



*/


Month month;

// Signal handler for SIGINT (Ctrl+C)
void handle_sigint(int sig) {
    printf("\nProgram interrupted...\n");
    // Perform cleanup 
    printf("Writing to file... \n");
    writingToFile("reminder.txt", month.reminders);
    printf("Reminders saved. Now exiting.\n");
    freeMonth(month);
    //flushBuffer();

    exit(0);  // Exit 
}

// Signal handler for SIGTERM (termination signal)
void handle_sigterm(int sig) {
    printf("\nProgram terminated...\n");
    // Perform cleanup 
    printf("Writing to file... \n");
    writingToFile("reminder.txt", month.reminders);
    printf("Reminders saved. Now exiting.\n");
    freeMonth(month);
    exit(0);  // Exit gracefully
}

// Set up the signal handlers
void setup_signal_handlers() {
    signal(SIGINT, handle_sigint);
    signal(SIGTERM, handle_sigterm);
}


int main(){
    

    
    setup_signal_handlers();

    // initializes month, reads any preexisitng reminders, and prints the calendar.
    month = initializeMonth();
    readingFromFile("reminder.txt", month.reminders); 
   

    char input[100];


    // remember: read_reminder should return 0 if and only if the user entered 0
    bool running = true;
    while (running == true){
       
        int result = read_reminder(input, sizeof(input));

        if (result == 0)
        {
            running = false;
        }
        if (result > 0)
        {
            print_calendar();
        }
        
    }
    
    // while (read_reminder(input, sizeof(input)) != 0){
        
        
        
    //     print_calendar();

    //     // printf("The reminders are as follows: \n");
    //     // print_reminders();
    // }

    printf("Savings reminders... \n");
    writingToFile("reminder.txt", month.reminders);
    printf("Reminders saved. Now exiting.\n");
    freeMonth(month);
    

    return 0;

}