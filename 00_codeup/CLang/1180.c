#include <stdio.h>

int main()
{	
	int n, temp;
	scanf("%d", &n);

	temp = (n%10)*10 + n/10;
	temp = temp * 2;
	temp = temp % 100;
	
	printf("%d", temp);
	printf("\n");

	if (temp > 50) {
		printf("OH MY GOD");
	}
	else {
		printf("GOOD");
	}
	return 0;
}