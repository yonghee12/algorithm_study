#include <stdio.h>

int main() {
    int i, j;
    scanf("%d", &n);

    for (i=0; i<n; i++) {
        for (j=0; j<=i; j++) {
            printf("*");
        }
        printf("\n");
    }
    for (i=n-1; j>0; i--) {
        for (j=0; j<i; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}