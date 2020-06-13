#include <stdio.h>

int main()
{
    int a[1001], n, k;
    scanf("%d", &n);
    for (int i=1; i<=n; i++)
    {
        scanf("%d", &a[i]);
    }
    for (int j=n; j>=1; j--)
    {
        printf("%d ", a[j]);
    }
}