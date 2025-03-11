#include <stdio.h>
#include <ctype.h>

/*
Write a C program that will convert a given quantity from one measuring unit to another.
First, the user is asked what she/he wants to do.
An integer can be entered with the following six actions associated with different values of the integer.
You can assume that the user will always enter an integer.
*/

int main()
{

    char conversionDirection;

    while (1)
    {
        int conversionType;
        printf("\n");
        printf("What conversion would you like to perform? \n");
        printf("1 for conversion between Grams and Ounces (1 gram == 0.03527 ounces) \n");
        printf("2 for conversion between Square meters and Square Yards (1 square meter == 1.19599 square yards)\n");
        printf("3 for conversion between Litres and Pints (1 litre == 2.11338 pints)\n");
        printf("4 for conversion between Meter and Feet (1 meter == 3.28084 feet)\n");
        printf("5 for quit\n");

        scanf(" %d", &conversionType);

        if (conversionType == 5)
        {
            return 0;
        }

        else if (conversionType == 1)
        {
            float numGrams;
            float numOunces;

            printf("G for conversion from Grams to Ounces \n");
            printf("O for conversion from Ounces to Grams \n");
            scanf(" %c", &conversionDirection);

            conversionDirection = toupper(conversionDirection);
            if (conversionDirection != 'G' && conversionDirection != 'O')
            {
                continue;
            }

            // 1 gram == 0.03527 ounces

            // Assignment instructions specify we assume the user will always enter valid floats.
            if (conversionDirection == 'G')
            {

                printf("Please enter the number of grams:\n");
                scanf(" %f", &numGrams);

                numOunces = numGrams * 0.03527; // performs the calculation
                printf("Your conversion is: %f grams to %4f ounces  \n", numGrams, numOunces);
                conversionDirection = 0;
            }
            else if (conversionDirection == 'O')
            {
                printf("Please enter the number of ounces:\n");
                scanf(" %f", &numOunces);

                numGrams = numOunces / 0.03527;
                printf("Your conversion is: %f ounces to %4f grams  \n", numOunces, numGrams);
                conversionDirection = 0;
            }

            printf(" \n");
        }
        else if (conversionType == 2)
        {
            float numSquareMeters;
            float numSquareYards;
            printf("M for conversion from Square Meters to Square Yards \n");
            printf("Y for conversion from Square Yards to Square Meters \n");

            scanf(" %c", &conversionDirection); // using scanf like this will ignore any leading whitespace

            conversionDirection = toupper(conversionDirection);

            if (conversionDirection != 'M' && conversionDirection != 'Y')
            {
                continue;
                ;
            }

            // Assignment instructions specify we assume the user will always enter valid floats.
            if (conversionDirection == 'M')
            {

                printf("Please enter the number of Square Meters:\n");
                scanf(" %f", &numSquareMeters);

                numSquareYards = numSquareMeters * 1.19599; // performs the calculation
                printf("Your conversion is: %f square meters to %4f square yards  \n", numSquareMeters, numSquareYards);
                conversionDirection = 0;
            }
            else if (conversionDirection == 'Y')
            {
                printf("Please enter the number of square yards:\n");
                scanf(" %f", &numSquareYards);

                numSquareMeters = numSquareYards / 1.19599;
                printf("Your conversion is: %f square yards to %f square meters  \n", numSquareYards, numSquareMeters);
                conversionDirection = 0;
            }
        }

        /// Case for conversion 3 between Litres and Pints
        else if (conversionType == 3)
        {

            float numLitres;
            float numPints;

            printf("L for conversion from Litres to Pints \n");
            printf("P for conversion from Pints to Litres \n");
            scanf(" %c", &conversionDirection);
            conversionDirection = toupper(conversionDirection);

            if (conversionDirection != 'L' && conversionDirection != 'P')
            {
                continue;
                ;
            }

            if (conversionDirection == 'L')
            {

                printf("Please enter the number of litres:\n");
                scanf(" %f", &numLitres);

                numPints = numLitres * 2.11338; // performs the calculation
                printf("Your conversion is: %f litres to %4f pints  \n", numLitres, numPints);
                conversionDirection = 0;
            }
            else if (conversionDirection == 'P')
            {
                printf("Please enter the number of pints:\n");
                scanf(" %f", &numPints);

                numLitres = numPints / 2.11338;
                printf("Your conversion is: %f pints to %4f litres  \n", numPints, numLitres);
                conversionDirection = 0;
            }
        }

        // Case for conversion 4 between meters and feet
        else if (conversionType == 4)
        {

            float numMetres;
            float numFeet;

            printf("M for conversion from Meters to Feet \n");
            printf("F for conversion from Feet to Meters \n");
            scanf(" %c", &conversionDirection);

            conversionDirection = toupper(conversionDirection);

            if (conversionDirection != 'M' && conversionDirection != 'F')
            {
                continue;
            }

            // 1 meter == 3.28084 feet
            // Assignment instructions specify we assume the user will always enter valid floats.
            if (conversionDirection == 'M')
            {
                printf("Please enter the number of metres:\n");
                scanf(" %f", &numMetres);

                numFeet = numMetres * 3.28084; // performs the calculation
                printf("Your conversion is: %f metres to %4f feet  \n", numMetres, numFeet);
                conversionDirection = 0;
            }
            else if (conversionDirection == 'F')
            {
                printf("Please enter the number of feet:\n");
                scanf(" %f", &numFeet);

                numMetres = numFeet / 3.28084;
                printf("Your conversion is: %f feet to %4f metres  \n", numFeet, numMetres);
                conversionDirection = 0;
            }
        }
        else
        {

            continue;
        }
    }

    return 0;
}
