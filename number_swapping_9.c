#include<stdio.h>
int main()
{
    int a,b;
    printf("enter 2 no.s");
    scanf("%d%d",&a,&b);
    a=a+b;
    b=a-b;
    a=a-b;
    printf(" swaped no.s are %d %d",a,b);

}