#include <stdio.h>
#include <string.h>

int main(void)
{
    printf("Do you Agree?\n");

    char c;
    scanf(" %c", &c);

    if (c == 'Y' || c == 'y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'N' || c == 'n')
    {
        printf("Not Agreed.\n");
    }
    return 0;
}