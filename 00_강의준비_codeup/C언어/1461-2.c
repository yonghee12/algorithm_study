#include <stdio.h>

int main() {
    int arr[100][100];
    int n, i, j;

    scanf("%d", &n);

    for (i=0; i<n; i++) {
        for (j=0; j<n; j++) {
            arr[i][j] = n*(i+1) - j;
        }
    }

    for (i=0; i<n; i++) {
        for (j=0; j<n; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }        

    return 0;
}