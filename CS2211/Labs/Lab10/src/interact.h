#ifndef INTERACT_H
#define INTERACT_H
#include "person.h"    // Make sure this file defines your structures/enums
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include "linked_list.h"

// Function declarations

void readName(char *name);
bool isValidFloat(const char* str);
void printMenu(void);
Choice getChoice(void);
RoleType getRole(void);
int getID(RoleType roleIn);
char* getName(void);
bool containsDigit(const char *str);
void deletePerson(Node** head);
void addPerson(Node** head);
void updatePerson(Node** head);
float getInfo(RoleType role);


// Signal handler function prototypes
void handle_sigint(int sig);
void handle_sigterm(int sig);

// Function to setup signal handlers
void setup_signal_handlers();



#endif // INTERACT_H
