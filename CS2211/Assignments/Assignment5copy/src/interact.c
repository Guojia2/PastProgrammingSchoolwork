
#include "linked_list.h"
#include "reminder.h"
#include "interact.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>


// Trims leading and trailing whitespace
void trim_whitespace(char *str) {
    char *start = str;
    while (isspace((unsigned char)*start)) {
        start++;
    }
    memmove(str, start, strlen(start) + 1);

    char *end = str + strlen(str) - 1;
    while (end > str && isspace((unsigned char)*end)) {
        *end = '\0';
        end--;
    }
}

void flushBuffer()
{
    int c;
    do
    {
        c = getchar(); // Read one character at a time
    } while (c != '\n' && c != EOF); // Stop when a newline or end of file is encountered
}

// this will probably be called as readingfromFile("reminders.txt", month.reminders)
void readingFromFile(const char *filename, Node *reminders[])
{ // reads reminders from a  file

    // opens the file in reading mode using fopens, and prints error if there is an error
    FILE *file = fopen(filename, "r");
    if (!file)
    {
        perror("Error opening file");
        return;
    }

    int day;
    char *task;
    // adds reminders to the linked list so long as fscanf is successfully reading reminders
    while (fscanf(file, "%d %[^\n]", &day, task) == 2)
    {   
        trim_whitespace(task);
        //printf("Task is: _%s__ \n", task);
        insert_to_calendar(day, task);
    }

    fclose(file);
}

void writingToFile(const char *filename, Node *reminders[])
{
    FILE *file = fopen(filename, "w");
    if (!file)
    {
        perror("Error opening file");
        return;
    }

    int i;
    // for every index in the array month.reminders[], iterate through the linked list at that index and print the contents of each node to teh file
    for (i = 0; i < month.month_days; i++){
        Node* current = month.reminders[i];
        while (current){
            char* text = strdup(current->data);

            fprintf(file, "%d %s \n", i + 1, text);
            //printf("%s", text);
            
            free(text);
            current = current->next;
        }
    }
    fclose(file);
}

