#include <stdio.h>

int main()
{
	int n, i, j;
	int arr[100][100];
	scanf("%d", &n);

	for (i=0; i<n; i++)
	{
		for (j=0; j<n; j++)
		{
			arr[i][j] = n*(i+1) - j; 
			printf("%d ", arr[i][j]);
		}
		printf("\n");
	}
}
