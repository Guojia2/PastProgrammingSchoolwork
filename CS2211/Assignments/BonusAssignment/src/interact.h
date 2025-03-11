/*
Interact.h/interact.c: Defines functions that interacts with the user. For example,
readReminder(), flushBuffer(), readingFromFile(), and writingToFile().
• linked_list.h/linked_list.c: Defines struct Node which holds one reminder



*/

#ifndef INTERACT_H
#define INTERACT_H

#include "linked_list.h"
#include "reminder.h"

// Function prototypes
void flushBuffer();                                  // Clears the input buffer
char* readReminder(char* buffer, size_t maxLen);    // Reads a reminder from the user
void readingFromFile(const char* filename, Node* reminders[]); // Reads reminders from a file
void writingToFile(const char* filename, Node* reminders[]);   // Writes reminders to a file
void trim_whitespace(char *str);

#endif // INTERACT_H
