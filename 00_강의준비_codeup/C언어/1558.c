#include <stdio.h>

long long int n;

long long int f(n)
{
    unsigned long long int temp, result;
    temp = 0;
    result = 0;
    while (n)
    {
        temp = n % 10;
        // printf("temp: %lld\n", temp);
        result = (result * 10) + temp;
        // printf("result: %lld\n", result);
        n = n / 10;
    }

    return result;
}

int main()
{
    scanf("%lld", &n);
//   printf("%lld\n", f(n));
    printf("%lld", f(n));
}