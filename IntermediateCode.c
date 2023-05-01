#include <stdio.h>
#include<string.h>
int main()
{
    int option;
    char str[1000],temp1[10]={0},temp2[10]={0};
    printf("Select the option: 1. Assignment 2. Arithmetic 3. Relational 4. Exit \n");
    scanf("%d",&option);
    printf("Enter the string\n");
    scanf("%s",str);
    switch(option)
    {
        case 1:
        {
            printf("Three address code: \n");
            printf("temp=%c\n",str[2]);
            printf("%c=temp\n",str[0]);
            break;
        }
        case 2:
        {
            temp1[0] = str[0];
            temp1[1] = str[1];
            temp1[2] = str[2];
            printf("Three address code: \n");
            printf("temp=%s",temp1);
            printf("\n");
            temp2[0]=str[3];
            temp2[1]=str[4];
            printf("temp1=temp%s\n",temp2);
            break;
        }
        case 3:
        {
            char id1,op1,op2,id2;
            id1 = str[0];
            op1 = str[1];
            op2 = str[2];
            id2 = str[3];
            int addr=100;
            printf("%d if %c %c %c %c goto %d\n",addr,id1,op1,op2,id2,addr+3);
            addr++;
            printf("%d T: = 0\n",addr);
            addr++;
            printf("%d go to %d\n",addr,addr+2);
            addr++;
            printf("%d T:= 1\n",addr);
            break;
        }
    }
    
    return 0;
}


//input for assignment a=b
//input for arithmetic a+b-c
//input for relatinal a<=b