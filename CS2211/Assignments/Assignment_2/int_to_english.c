#include <stdio.h>

int main()
{
    // Arrays to store words for specific numbers
    char *singleDigits[] = {"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    char *teenDigits[] = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    char *tensDigits[] = {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

    int number;

    while (1) {

        printf("Please enter a value (1-999, 0 to quit): ");
        scanf(" %d", &number);

        if (number == 0) {
            printf("Program terminated. Coward.\n");
            break;
        }

        printf("You entered the number ");
        
        if (number >= 100) {
        printf("%s hundred", singleDigits[number / 100]);
        number = number% 100;

        if (number != 0) {
            printf(" and ");
        }
    }

    if (number >= 20) {
        printf("%s", tensDigits[number / 10]);
        if (number % 10 != 0) {
            printf("-%s", singleDigits[number % 10]);
        }
    }
    else if (number >= 10) {
        printf("%s", teenDigits[number - 10]);
    }
    else if (number > 0) {
        printf("%s", singleDigits[number]);
    }
        printf("\n");
    }




    return 0;
}