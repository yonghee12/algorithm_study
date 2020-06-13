#include <stdio.h>

int main() {
    int arr[100][100];
    int n, m, i, j;

    scanf("%d", &n);
    scanf("%d", &m);

    for (i=0; i<n; i++) {
        for (j=0; j<m; j++) {
            arr[i][j] = m*(n-i-1)+1 + j;
        }
    }

    for (i=0; i<n; i++) {
        for (j=0; j<m; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }        

    return 0;
}