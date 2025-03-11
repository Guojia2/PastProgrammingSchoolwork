#include <stdio.h>

int main(){
	int daysInMonth;
	int startingDay;
	

	printf("Enter number of days in month:\n");
	scanf("%d", &daysInMonth);

	printf("Enter starting day of the week (1=Sun, 7=Sat)\n");
	scanf("%d",&startingDay);

	for (int i = 0; i < startingDay; i++){
		printf(" ");
	}

	for(int i = 1; i <= daysInMonth; i++){
		printf("%3d", i);

		if ((i + startingDay - 1) % 7 == 0) {
           	 	printf("\n");
	}
	}
	printf("\n");
	return 0;
}

