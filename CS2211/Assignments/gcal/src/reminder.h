#ifndef REMINDER_H
#define REMINDER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include "linked_list.h"

#define MAX_STR_LEN 100




enum MonthEnum {
    January = 1,
    February,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    October,
    November,
    December
};
struct Month{
	int month_days;
	int start_day;
	enum MonthEnum month_idx;
	Node* reminders[31];
	bool hasReminder[31];
};


typedef struct Month Month;
extern  Month month; 


/*
Takes a reminder string and a day number and inserts the reminder into the calendar.
Also, sets the reminder flag to true for that day.
 */
void insert_to_calendar(int day, const char* value) ;
void removeReminder(int day, const char* value);

/*
Takes the command line args argc and argv and reads the reminder and puts it into the calendar
 */
int read_reminder(int argc, char* argv[]) ;

/*
Prints the calendar and the reminders for each day.	
 */
void print_calendar() ;

Month initializeMonth(void); // initializes the extern month struct

void print_reminders();
void printToday(); 
void freeMonth(Month month); // frees the month struct
const char* getMonthName(enum MonthEnum month); //helper function to convert the enum month into a month string

#endif