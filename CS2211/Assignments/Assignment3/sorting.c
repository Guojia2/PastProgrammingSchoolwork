#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// this function swaps the values stored at the memory locations pointed at by *a and *b.
// in this context of this program, it will be used to swap elements in an array.
void swap(int *a, int *b)
{

    int temp = *a;
    *a = *b;
    *b = temp;
}

// this function partitions arrays and subarrays
int Partition(int arr[], int lowIndex, int highIndex) {
    int pivot = arr[highIndex];
    int i = lowIndex - 1;

    for (int j = lowIndex; j < highIndex; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[highIndex]);
    return i + 1;
}

void BubbleSort(int arr[], int length)
{
    // length is the number of elements in the array, not the number of bytes the array uses.

    int i;
    int j;
    for (i = 0; i < length; i++)
    {
        for (j = 0; j < length - i - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                // Swap if they are in the wrong order
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
    return;
}

void QuickSort(int arr[], int lowIndex, int highIndex)
{

    /*

    quicksort:

    1. Pick a pivot ( we will use last element of array)
    2. Partition the array. This means that we must move elements of the array around such that the pivot value is in its correct place.
    3. call quicksort again, this time on the next element of the array.




    */

    if (lowIndex < highIndex)
    {
        // Partition() returns the index of the pivot element in its sorted place
        int partitionIndex = Partition(arr, lowIndex, highIndex);

        // recursively calls QuickSort() on the left and right subarrays;
        QuickSort(arr, lowIndex, partitionIndex - 1);
        QuickSort(arr, partitionIndex + 1, highIndex - 1);
    }

    return;
}

int main()
{

    int arrayLength;
    int n;
    char command;
    int initialized = 0; // this flag is used to checkl whether teh program has initialized an array yet

    do
    {

        if (!initialized || command == 'N')
        {
            // prompts user for number of elements and array length
            printf("How many numbers will you input? Please enter an even number: ");
            scanf(" %d", &n);
            printf("Please enter your array length. It must be even and equal to or greater than the number of numbers: ");
            scanf(" %d", &arrayLength);

            if (n > arrayLength || n % 2 != 0 || arrayLength % 2 != 0)
            {
                printf("Error: n and m must be even numbers, and m >= n.\n");
                continue;
            }

            int numbers[2][arrayLength];
            // repeatedly prompts user for numbers
            int i;
            for (i = 0; i < n; i++)
            {
                printf("Please input a number ");
                scanf(" %d", &numbers[0][i]);
            }

            // fills remaining slots of first row of array with random numbers
            if (n < arrayLength)
            {
                for (; i < arrayLength; i++)
                {
                    // Modulo is used to put a cap on the maximum value of rand() because extremely large values are unneccessary and inconvenient
                    numbers[0][i] = rand() % 1001;
                }
            } 

            // copies the unsorted first row row into the second row.
            // The second row will be passed as its own array to the sorting functions.
            for (i = 0; i < arrayLength; i++)
            {
                numbers[1][i] = numbers[0][i];
            }

            // prompts user to choose their sorting algorithm
            if (command == 'S' || command == 'N' || command == 'R' || !initialized )
            {
                int sortingAlgorithmChoice;
                printf("Choose a sorting algorithm: \n (0) Quick sort (1) Bubble sort \n");
                scanf(" %d", &sortingAlgorithmChoice);

                time_t time1;
                time_t time2;
                time_t deltaTime;

                if (sortingAlgorithmChoice == 0)
                {
                    time1 = time(NULL);

                    QuickSort(numbers[1], 0, arrayLength - 1);

                    time2 = time(NULL);
                    deltaTime = time2 - time1;
                }

                else if (sortingAlgorithmChoice == 1)
                {
                    time1 = time(NULL);

                    BubbleSort(numbers[1], arrayLength - 1);

                    time2 = time(NULL);
                    deltaTime = time2 - time1;
                }

                printf("Raw Array: \n");
                for (int i = 0; i < arrayLength; i++)
                {
                    printf("%6d", numbers[0][i]);
                }
                printf("\n");

                printf("Sorted Array: \n");
                for (int i = 0; i < arrayLength; i++)
                {
                    printf("%6d", numbers[1][i]);
                }

                printf("\n");

                printf("Sorting Duration (sec): %ld", deltaTime);
            }

            initialized = 1;
            // Command options
            printf("\nEnter a command:\n");
            printf("(R) Re-generate different random numbers and choose a different sorting algorithm.\n");
            printf("(N) Enter new values for n and m, and enter new n numbers.\n");
            printf("(S) Use a different sorting algorithm to sort the same array.\n");
            printf("(Q) Quit.\n");
            printf("Your choice: ");
            scanf(" %c", &command);

            // Handle command actions
            if (command == 'R' || command == 'r')
            {
                // Re-generate different random numbers in the second row and choose a new sorting algorithm
                for (int i = n; i < arrayLength; i++)
                {
                    numbers[0][i] = rand() % 1001;
                    numbers[1][i] = numbers[0][i]; // Copy to the second row for sorting
                    continue;
                }
            }
            else if (command == 'N' || command == 'n')
            {
                // Reset values and loop back to enter new n and arrayLength
                continue;
            }
            else if (command == 'S' || command == 's')
            {   
                continue;
                // Prompt for a different sorting algorithm on the same array
            }
            else if (command == 'Q' || command == 'q')
            {
                printf("Exiting program.\n");
                break;
            }
            else
            {
                printf("Invalid command. Exiting program.\n");
                break;
            }
        }

    } while (1);

    return 0;
}
