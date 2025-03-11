#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

void encrypt(char *message, int shift)
{

   for (int i = 0; message[i] != '\0'; i++) {
        char ch = message[i];
        
        // Shift uppercase letters
        if (isupper(ch)) {
            message[i] = 'A' + (ch - 'A' + shift + 26) % 26;
        }
        // Shift lowercase letters
        else if (islower(ch)) {
            message[i] = 'a' + (ch - 'a' + shift + 26) % 26;
        }
        // Leave spaces and other characters unchanged
    }
}


int main(int argc, char *argv[])
{
    if (argc < 3)
    {
        printf("Not enough arguments");
        return 1;
    }

    // argv is an array of pointers to strings

    // this for-loop counts up the total number of characters in our original message
    int messageLength = 0;
    for (int i = 0; i < argc - 1; i++)
    {
        messageLength += strlen(argv[i]) + 1; // +1 to account for the space character between each argument
    }

    // Now, we must build a string containing our message.
    char message[messageLength];
    strcpy(message, argv[1]);
    // we start i at 2 because the 0th argument is ./encrypt and the 1st argument is already in message
    // we increment i up until argc - 1 because we do not want to include the shift value in message
    for (int i = 2; i < argc - 1; i++)
    {
        // appends a space character and the following argument to message
        strcat(message, " ");
        strcat(message, argv[i]);
    }

    // this line takes the final argument, converts it to an integer, then stores it in shiftValue
    int shiftValue = atoi(argv[argc - 1]);

        encrypt(message, shiftValue);

    printf("Encrypted message: %s\n", message);

    return 0;

}