#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

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
    EXIT
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

// Global array of people and count
Person people[MAX_PEOPLE];
int numPeople = 0;

int findPersonIndex(RoleType role, int id);

// This is a custom string reading function. It will read and discard white-spaces that are
// found in the buffer before characters. It will read until it finds a ‘\n’, but will only store up to
// 50 characters in the character array passed as argument.
void readName(char *name)
{
    getchar(); // Clear newline from previous input
    fgets(name, MAX_NAME_LENGTH, stdin);

    // Trim leading spaces
    int start = 0;
    while (isspace(name[start]))
    {
        start++;
    }

    // Copy the trimmed name to the beginning of the array
    memmove(name, name + start, strlen(name) - start + 1);

    // Remove trailing newline character
    name[strcspn(name, "\n")] = '\0';
}

bool containsDigit(const char *str)
{
    int length = strlen(str); // Get the length of the string
    for (int i = 0; i < length; i++)
    { // Loop through each character by index
        if (isdigit((unsigned char)str[i]))
        {
            return true; // Return true if a digit is found
        }
    }
    return false; // Return false if no digits are found
}

// prints the menu options to the user
void printMenu(void)
{
    printf("\n");
    printf("_______________________\n");
    printf("\nMenu:\n");
    printf("\n");
    printf("1. Add a person\n");
    printf("2. Update a person\n");
    printf("3. Print all people\n");
    printf("4. Delete a person\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
}

// reads and validates the user's choice from the menu.
// returns an enum value corresponding to the user's choice.
Choice getChoice(void)
{
    int choice;
    if (scanf("%d", &choice) != 1 || choice < 1 || choice > 5)
    {
        while (getchar() != '\n')
            ;      // clear invalid input
        return -1; // invald choice
    }
    return (Choice)(choice - 1); // adjust for enum indexing
}

// This function takes a role and an id and returns a Boolean. It checks if the given role and
// id matches with a person in the array, if a match is found, the function returns true.
// Otherwise, it returns false.
bool personExists(RoleType role, int id)
{
    for (int i = 0; i < numPeople; i++)
    {
        if (people[i].role == role)
        {
            if ((role == STUDENT && people[i].info.student.StudentId == id) || (role == PROFESSOR && people[i].info.professor.ProfessorId == id))
            {
                return true;
            }
        }
    }
    return false;
}

// Asks for the role of the person to be added. Depending on the entered role, it will ask the
// user for the student details or the professor details. If a person with the same role and ID
// exists in the array, the function will not add this new person.
void addPerson(void)
{
    if (numPeople >= MAX_PEOPLE)
    {
        printf("Error: Cannot add more people, storage is full.\n");
        return;
    }

    Person newPerson;
    int id;
    int roleInput;

    printf("Enter role (0 for Student, 1 for Professor): ");
    if (scanf("%d", &roleInput) != 1 || (roleInput != STUDENT && roleInput != PROFESSOR))
    {
        printf("Invalid role type. Please enter 0 for Student or 1 for Professor.\n");
        while (getchar() != '\n')
            ; // Clear invalid input
        return;
    }
    newPerson.role = (RoleType)roleInput;

    do
    {
        printf("Enter name: ");
        readName(newPerson.name);
        if (containsDigit(newPerson.name))
        {
            printf("Invalid name. Name cannot contain numbers");
        }
        else
        {
            break;
        }

    } while (true);

    do
    {
        printf("Enter Student ID: ");
        
        int result = scanf("%d", &id);

        // scanf will return 1 if it reads an integer, so we can check whether the user inputted an integer this way
        if (result != 1)
        {
            printf("Invalid ID. ID must be a postitive number. \n");
        }
        // checks if user inputted an id that is a postive number
        else if (id <= 0)
        {
            printf("Invalid ID. ID must be a positive number. \n");
        }
        else
        {
            break;
        }

    } while (true);


    if (newPerson.role == STUDENT)
    {
        if (personExists(STUDENT, id))
        {
            printf("Error: Student ID already exists.\n");
            return;
        }
        newPerson.info.student.StudentId = id;

        printf("Enter GPA: ");

        while (scanf("%f", &newPerson.info.student.GPA) != 1){
            printf("Invalid GPA. GPA must be a positive number. \n");
            printf("Enter GPA: ");
        }

        printf("Person added successfully.\n");
    }

    else if (newPerson.role == PROFESSOR)
    {

        do
        {
            printf("Enter Professor ID: ");
            scanf("%d", &id);

            if (id <= 0)
            {
                printf("Invalid ID. ID must be a postitive number. \n");
            }

        } while (id <= 0);

        if (personExists(PROFESSOR, id))
        {
            printf("Error: Professor ID already exists.\n");
            return;
        }
        newPerson.info.professor.ProfessorId = id;

        printf("Enter Salary: ");
        scanf("%lf", &newPerson.info.professor.salary);
        printf("Professor added successfully.\n");
    }

    people[numPeople++] = newPerson;
}

/*Asks the user for the role and id of the person to be updated.
Then it searches for that person in the array.
If the person exists, the function will allow the user to update all the details of this person using new info entered by the user.
The information to be updated if the person is a student are (name, id, GPA), if the person is a professor, the information to be updated are (name, id, salary).
*/
void updatePerson(void)
{
    int roleInput;
    int id;
    char newName[MAX_NAME_LENGTH];
    Person *person;

    printf("Enter role (0 for Student, 1 for Professor): ");
    if (scanf("%d", &roleInput) != 1 || (roleInput != STUDENT && roleInput != PROFESSOR))
    {
        printf("Invalid role type. Role must be either 0 or 1\n");
        while (getchar() != '\n')
            ; // Clear invalid input
        return;
    }

    printf("Enter ID: ");
    scanf("%d", &id);
    
    printf("Enter Name");
    scanf("%s", newName);
    // The variable newName won't actually be used to find the person
    //, since that would require redoing multiple entire funcitons
    // im just prompting the user for a name to fulfill program requirements


    // checks if the person exists

    if (!personExists(roleInput, id))
    {
        printf("Error: Person not found.\n");
    }
    else
    {
        int index = findPersonIndex(roleInput, id);
        person = &people[index];

        // Prompt for new person information
        if (person->role == STUDENT)
        {
            printf("Enter new GPA: ");
            scanf("%f", &person->info.student.GPA);

            printf("Student updated successfully");
        }
        else if (person->role == PROFESSOR)
        {
            printf("Enter new Salary: ");
            scanf("%lf", &person->info.professor.salary);

            printf("Professor updated successfully");
        }
    }

}

// The function asks the user for the role and id of a person in the database. If a match is
// found, the item will be removed from the array.
void deletePerson(void)
{

    if (numPeople == 0)
    {
        printf("Error: Cannot delete people, database is empty.\n");
        return;
    }

    Person targetPerson;
    int id;
    int roleInput;
    RoleType targetRole;

    printf("Enter role of the person to be deleted (0 for Student, 1 for Professor): ");
    if (scanf("%d", &roleInput) != 1 || (roleInput != STUDENT && roleInput != PROFESSOR))
    {
        printf("Invalid role type. Please enter 0 for Student or 1 for Professor.\n");
        while (getchar() != '\n')
            ; // Clear invalid input
        return;
    }

    targetRole = (RoleType)roleInput;

    if (targetRole == STUDENT)
    {
        printf("Enter Student ID: ");
        scanf("%d", &id);

        for (int i = 0; i < numPeople; i++)
        {
            if (people[i].info.student.StudentId == id && people[i].role == targetRole)
            {
                people[i] = people[i] = (Person){0};

                numPeople--;
                printf("Student deleted successfully.\n");
                return;
            }
        }
    }
    else if (targetRole == PROFESSOR)
    {
        printf("Enter Professor ID: ");
        scanf("%d", &id);

        for (int i = 0; i < numPeople; i++)
        {
            if (people[i].info.professor.ProfessorId == id && people[i].role == targetRole)
            {
                people[i] = people[i] = (Person){0};
                numPeople--;
                printf("Professor deleted successfully.\n");
                return;
            }
        }
    }
}

// prints the information of the given person.
// When p is a pointer to a struct, you can access the members of this struct using the arrow operator (->)
void printPerson(const Person *p)
{
    printf("Name: %s\n", p->name);
    if (p->role == STUDENT)
    {
        printf("Role: Student\n");
        printf("Student ID: %d\n", p->info.student.StudentId);
        printf("GPA: %.2f\n", p->info.student.GPA);
    }
    else if (p->role == PROFESSOR)
    {
        printf("Role: Professor\n");
        printf("Professor ID: %d\n", p->info.professor.ProfessorId);
        printf("Salary: %.2f\n", p->info.professor.salary);
    }
}

// this function takes a person's role and type and then finds that person in the array of poeple
int findPersonIndex(RoleType role, int id)

{

    for (int i = 0; i < numPeople; i++)
    {
        if (people[i].role == role)
        {
            if ((role == STUDENT && people[i].info.student.StudentId == id) || (role == PROFESSOR && people[i].info.professor.ProfessorId == id))
            {
                return i;
            }
        }
    }
    return -1;
}

int main(void)
{
    Choice choice;

    // Main program loop
    while (1)
    {
        printMenu();
        choice = 0;
        choice = getChoice();

        switch (choice)
        {
        case ADD:
            addPerson();
            break;
        case UPDATE:
            updatePerson();
            break;
        case PRINT:

            for (int i = 0; i < numPeople; i++)
            {
                Person *p = &people[i];
                printPerson(p);
                printf("\n");
            }

            break;
        case DELETE:
            deletePerson();
            break;
        case EXIT:
            printf("Exiting program.\n");
            return 0;
        default:
            printf("Invalid choice. Please try again.\n");
        }
    }
    return 0;
}
