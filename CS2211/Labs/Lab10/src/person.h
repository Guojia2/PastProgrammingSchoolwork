#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>


#ifndef PERSON_H  // If PERSON_H is not defined
#define PERSON_H  // Define PERSON_H to avoid multiple inclusions

// defining constants
#define MAX_NAME_LENGTH 51
#define MAX_PEOPLE 100

// enum for role type
typedef enum
{
    STUDENT,
    PROFESSOR
} RoleType;

// enum for menu choices
typedef enum
{
    ADD,
    UPDATE,
    PRINT,
    DELETE,
    EXIT,
    INVALID
} Choice;

// Structs for student and professor info
typedef struct
{
    int StudentId;
    float GPA;
} StudentInfo;

typedef struct
{
    int ProfessorId;
    double salary;
} ProfessorInfo;

// Union for storing student or professor-specific data
typedef union
{
    StudentInfo student;
    ProfessorInfo professor;
} PersonInfo;

// Struct for a person
typedef struct
{
    RoleType role;
    char name[MAX_NAME_LENGTH];
    PersonInfo info;
} Person;




#endif // PERSON_H