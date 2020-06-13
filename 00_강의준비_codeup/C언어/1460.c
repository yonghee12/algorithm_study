#include <stdio.h>

int main()
{
    int n, i, j;
    int k=1;
    int arr[100][100];
    scanf("%d", &n);
    
    for (i=0; i<n; i++)
    {
        for (j=0; j<n; j++)
            arr[i][j] = k++;
    }

    for (i=0; i<n; i++)
    {
        for (j=0; j<n; j++)
            printf("%d ", arr[i][j]);
        printf("\n");
    }
}