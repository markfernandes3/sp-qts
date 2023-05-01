#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void main()
{
    char opcode[10], mnemonic[10], operand[10], operand1[10], label[10], code[10], address[10],sizeAddress[10], Motlabel[10];
    int locctr = 0, start, length, flag = 0;
    FILE *fp1, *fp2, *fp3, *fp4, *fp5, *fp6, *fp411;
    fp1 = fopen("inputAssembler.txt", "r");
    fp2 = fopen("sym_table.txt", "r");
    fp3 = fopen("out.txt", "r");
    fp4 = fopen("MOT.txt", "r");
    fp411 = fopen("MOT.txt", "r");
    fp5 = fopen("BT.txt", "w");
    fp6 = fopen("outTable.txt", "w");

    fscanf(fp1, "%s %s %s", label, opcode, operand1);

    if (strcmp(opcode, "START") == 0)
        fscanf(fp1, "%s %s %s", label, opcode, operand1);
    else
        locctr = 0;
    while (strcmp(opcode, "END") != 0)
    {
        fscanf(fp4, "%s", mnemonic);
        fscanf(fp411, "%s", Motlabel);
        while (strcmp(Motlabel, opcode) != 0 && strcmp(Motlabel, "end") != 0)
            fscanf(fp411, "%s", Motlabel);
        fscanf(fp411, "%s", Motlabel);
        if (strcmp(Motlabel, "end") != 0)
        {
            char sub = operand1[0];
            char substring[4];
            int j = 0;
            for (int i = 2; i < 6; i++)
                substring[j++] = operand1[i];
            fprintf(fp6, "%s %c, ", Motlabel, operand1[0]);
            for (int i = 0; i < 4; i++)
                fprintf(fp6, "%c", substring[i]);
            fprintf(fp6, "\n");
        }
        rewind(fp411);
        if (strcmp(opcode, "DC") == 0)
        {
            locctr += (operand[0] == 'F')? 4:2;
            fprintf(fp6, "%d %c\n", locctr, operand1[2]);
        }
        else if (strcmp(opcode, "DS") == 0)
        {
            locctr += (operand[1] == 'F')? 4:2;
            fprintf(fp6, "%d _\n", locctr);
        }
        else if (strcmp(opcode, "USING") == 0)
        {
            locctr += 0;
            fprintf(fp5, "%c%c", operand1[2], operand1[3]);
        }
        while (strcmp(mnemonic, "end") != 0)
        {
            if (strcmp(opcode, mnemonic) == 0)
            {
                locctr += 4;
                flag = 1;
                break;
            }
            fscanf(fp4, "%s", mnemonic);
        }
        flag = 0;
        fscanf(fp1, "%s %s %s", label, opcode, operand1);
        rewind(fp4);
    }
}