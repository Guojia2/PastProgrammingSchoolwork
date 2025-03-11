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

/*
Takes a char array and its length and reads a reminder from the user.
Returns the day number.
 */
int read_reminder(char str[100], int n) ;

/*
Prints the calendar and the reminders for each day.	
 */
void print_calendar() ;

Month initializeMonth(void); // initializes the extern month struct

void print_reminders();
void freeMonth(Month month); // frees the month struct
const char* getMonthName(enum MonthEnum month); //helper function to convert the enum month into a month string

#endif