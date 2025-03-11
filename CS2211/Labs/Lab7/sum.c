#include <stdio.h>

#include <stdlib.h>

int main(int argc, char *argv[])
{
    int sum = 0;

    // for each argument in the command, we want to convert the agrument into an integer and add it to sum
    // we start the loop at i = 1 becauwe the first "argument" is the name of the program
    for (int i = 1; i < argc; i++)
    {
        int num = atoi(argv[i]);
        sum += num;
    }

    // prints the sum and returns 
    printf("Sum: %d\n", sum);

    return 0;
}
