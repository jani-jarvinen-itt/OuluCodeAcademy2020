#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[15];
    int pass = 0;

    printf("Enter the password:\n");
    gets(buff);

    if (strcmp(buff, "supersecret"))
    {
        printf("Wrong password!\n");
    }
    else
    {
        printf("Correct password was given\n");
        pass = 1;
    }

    if (pass)
    {
       /* Now give root rights to user*/
        printf ("Root privileges given to the user\n");
    }

    return 0;
}
