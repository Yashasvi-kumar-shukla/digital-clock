#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <windows.h>

int main()
{
    int h=0,m=0,s=00;
    printf("enter your time like this format HH:MM:SS\n");
    scanf("%d:%d:%d",&h,&m,&s);

    start:;
    for(h;h<24;h++){
        for(m;m<60;m++){
            for(s;s<60;s++){
                system("cls");
                printf("\n\n\n\n\n\n\t\t\t\t\t\t %5d:%5d:%5d",h,m,s);
                sleep(1);
            }
            s=0;
        }
        m=0;
    }
    h=0;
    goto start;
}
