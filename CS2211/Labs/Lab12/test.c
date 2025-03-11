//read_numbers.c
#include <stdio.h>
#include <string.h>

int main() {
// int a = 1, b = 2;
// int c = 3;
// float x = 4, y = 5;
// char str[5] = "hello";
// int z = scanf("%2d %3o %4x %4s %*c %2f %*2c %3f", &a, &b, &c, str, &x, &y);

// printf("%d\n", a);
// printf("%d\n", b);
// printf("%d\n", c);
// printf("%s\n", str);
//  printf("%.2f\n", x);
// printf("%.2f\n", y);
// printf("%d\n", z);
// return 0;

char *str1 = "capitalZ";
char str2[10] = "capitalZ";
int length1 = strlen(str1);
int length2 = strlen(str2);


printf("%lu \n", sizeof(str1));
printf("%lu \n", sizeof(str2));



printf("%d", length1);
printf("\n");
printf("%d",length2);
printf("\n");




}
