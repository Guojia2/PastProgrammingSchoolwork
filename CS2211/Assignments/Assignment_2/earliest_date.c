#include <stdio.h>

int main()
{

    int month;
    int day;
    int year;

    int earliestMonth;
    int earliestDay;
    int earliestYear;

    int isFirstDate = 1; // use this variable to check if a date is the first and only date entered

    while (1)
    {
        printf("Enter a date (mm/dd/yy): ");
        scanf("%d/%d/%d", &month, &day, &year);

        // exits while loop if 0/0/0 is inputted
        if (month == 0 && day == 0 && year ==  0)
        {
            break;
        }


        if (isFirstDate) // set the first date to the earliest by default
        {
            earliestMonth = month;
            earliestDay = day;
            earliestYear = year;
            isFirstDate = 0; // turns off the flag so the program knows any further dates entered are not the first date
        }

        // Compare other dates and see which one is earlier
        else
        {
            // start by comparing year
            if (year < earliestYear)
            {
                earliestYear = year;
                earliestMonth = month;
                earliestDay = day;
            }
            // If the year is the same, compare month
            else if (year == earliestYear)
            {
                if (month < earliestMonth)
                {
                    earliestMonth = month;
                    earliestDay = day;
                }
                // If the month is also the same, compare the day
                else if (month == earliestMonth && day < earliestDay)
                {
                    earliestDay = day;
                }
            }
        }
    }   

        // These statements will be reached only after 0/0/0 is inputted by the user:

        // checks that at least one valid date was entered 
        if (!isFirstDate)
        {
            printf("%.2d/%.2d/%.2d is the earliest date\n", earliestMonth, earliestDay, earliestYear);
        }

        else
        {
            printf("No valid dates were entered.\n");
        }

    
    return 0;
}