#include <stdio.h>

int main()
{
    float f;
    scanf("%f", &f);
    
    if (f>=50 && f<=60)
    {
        printf("win");
    }
    else
    {
        printf("lose");
    }
    return 0;
}