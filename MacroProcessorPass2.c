#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
char opcode[10], mnemonic[10], operand[10], label[10], normal[10];
FILE *fp1, *fp2, *fp3, *fp4;
fp1 = fopen("INPUTMacro.txt", "r");
fp2 = fopen("Expanded Source.txt", "w");
fp3 = fopen("MNT.txt", "r");
fp4 = fopen("MDT.txt", "r");
fscanf(fp1, "%s %s %s", label, opcode, operand);
while (strcmp(opcode, "END") != 0)
{
if (strcmp(label, "Macro") == 0)
{
while (strcmp(label, "MEND") != 0)
{
fscanf(fp1, "%s %s %s", label, opcode, operand);
}
}
else if (strcmp(opcode, "START") == 0)
{
fprintf(fp2, "%s\t %s\t %s\n", label, opcode, operand);
fscanf(fp1, "%s %s %s", label, opcode, operand);
}
// fscanf(fp3, "%s", mnemonic);
// printf("%s", mnemonic);
else
{
if (strcmp(label, "**") == 0 && strcmp(operand, "**") == 0)
{
fscanf(fp4, "%s %s", mnemonic, normal);
printf("%s", mnemonic);
while (strcmp(opcode, mnemonic) != 0)
{
fscanf(fp4, "%s %s", mnemonic, normal);
}
if (strcmp(opcode, mnemonic) == 0)
{
while (strcmp(label, "MEND") != 0)
{
fscanf(fp4, "%s %s", label, opcode);
if (strcmp(opcode, mnemonic) == 0 || strcmp(label, "MEND") == 0)
{
continue;
}
   printf("%s\n", label);
fprintf(fp2, "%s %s\n", label, opcode);
}
rewind(fp4);
}
}
else
{
fprintf(fp2, "%s\t %s\t %s\n", label, opcode, operand);
}
}
rewind(fp3);
fscanf(fp1, "%s %s %s", label, opcode, operand);
}
fprintf(fp2, "%s\t %s\t %s\n", label, opcode, operand);
return 0;
}
