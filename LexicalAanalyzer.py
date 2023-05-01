def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
    

keywords = "auto break case char const continue default do double else enum extern float for goto if int long register return short signed sizeof static struct switch typedef union unsigned void volatile while"

kwList = keywords.split()

operators = "+ - * / % ++ -- < = <= > >= == != && || ! ?: & | << >> ~ ^ += -= *= /= %= "

oplist = operators.split()

schar = "{ } ( ) $ @ ;"

scharlist = schar.split()

inputFile = open('input.txt', 'r' )

tokens = inputFile.read().split()

for token in tokens:
    if token in kwList:
        print(token,"is keyword")
    elif token in oplist:
        print(token,"is operator")
    elif token in scharlist:
        print(token,"is special symbol")
    elif token.isdigit() or isfloat(token):
        print(token,"is constant")
    elif token[0]=='"' or token[0]=="'":
        print(token,"is literal")
    else :
        print(token,"is identifier")


""" input.txt

int a ;
float b = 10.2 ;
char ch = 'z' ;
char d = "strings" ;
int d = a * b ;

 """
