#include <stdio.h>

int main (int argc, char *argv[]){


    // Check if there are any arguments to reverse
    // we use argc > 1 because the program name is included in the argument count
    if (argc > 1) { 
        printf("Reversed message: ");
        
        // Loop through the arguments in reverse order
        for (int i = argc - 1; i > 0; i--) {
            printf("%s", argv[i]);

            // Print a space between words, but not after the last word
            if (i > 1) {
                printf(" ");
            }
        }
        printf("\n");
    } 

    return 0;
}




