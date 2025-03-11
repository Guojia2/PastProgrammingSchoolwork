#include <stdio.h>

// defining a function that converts minutes into 12-hour time and prints it
void ConvertTime(int timeInMinutes)
{
    //printf("ConverTime was used \n");
    //printf("timeinMinutes is %d \n", timeInMinutes);
    int hours = timeInMinutes / 60; 
    int minutes = timeInMinutes % 60;
    // printf("hours is %d\n", hours);
    // printf("minutes is %d\n", minutes);


    // now we must decide whether to use AM or PM
    if (hours >= 12 && hours < 24)
    {
        if (hours > 12)
        {
            hours = hours - 12;
            //printf("hours was reduced by 12\n");
        }
        printf("%d:%02d p.m.", hours, minutes);
        //printf("this branh was reached\n");
    }

    else if (hours >= 0 && hours < 12 || hours == 24)
    {
        printf("%d:%02d a.m.", hours, minutes);
    }
}

int main()
{

    int minutes;
    int hours;
    int totalMinutes;

    const int departures[] = {480, 583, 679, 767, 840, 945, 1140, 1305}; // In minutes
    const int arrivals[] = {616, 712, 811, 900, 968, 1075, 1160, 1438};  // In minutes
    const int departuresLength = sizeof(departures) / sizeof(departures[0]);

    int keepRunning = 1; // this variable will be used to check whether the program should loop around and ask for more user input

    while (keepRunning == 1)
    {

        // receive and store user input for their desired departure time
        printf("Enter a 24-hour time: \n");
        scanf("%d:%d", &hours, &minutes);

        totalMinutes = hours * 60 + minutes;

        // now we need to find the

        int nearestDeparture;
        int nearestArrival;

        for (int i = 0; i < departuresLength; i++)
        {
            if (totalMinutes <= departures[i])
            { // the array departures is sorted already, so we can look for the first element later than the user's input
                nearestDeparture = departures[i];
                nearestArrival = arrivals[i];
                break;
            }
        }

        if (totalMinutes > departures[departuresLength - 1])
        { // now we must handle the edge case where the user's input is later than all departures
            nearestDeparture = departures[0];
            nearestArrival = arrivals[0];
        }

        // print out the next available flight
        printf("Closest departure time is ");
        ConvertTime(nearestDeparture);
        printf(", arriving at ");
        ConvertTime(nearestArrival);
        printf("\n");

        // Prompt the user to continue or exit
        printf("Enter 1 to continue or anything else to quit: ");
        scanf("%d", &keepRunning);
    }
    return 0;
}