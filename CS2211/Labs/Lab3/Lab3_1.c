#include <stdio.h>

int main() {
	int a;
	int b;
	int c;
	int d;
	int largest;
	int smallest;

	printf("Enter four integers: ");
	scanf("%d %d %d %d", &a, &b, &c, &d);

	largest = smallest = a;

	if (b > largest){
		largest = b;
	}
	if (b < smallest){
		smallest = b;
	}

	if (c > largest){
		largest = c;
	}
	if (c < smallest){
		smallest = c;
	}

	if (d > largest){
		largest = d;
	}
	if (d < smallest){
		smallest = d;
	}


	printf("Largest: %d\n",largest);
	printf("Smallest %d\n", smallest);


	return 0;

}

