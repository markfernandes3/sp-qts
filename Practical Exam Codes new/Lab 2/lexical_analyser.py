keywords = ['int', 'break', 'else', 'long', 'switch', 'case', 'char', 'return', 'continue',
            'for', 'void', 'do', 'if', 'while', 'default', 'goto', 'sizeof', 'float', 'short']
operators = ['+', '-', '*', '/', '%', '<', '>', '=', '&', '|']
special_char = [';', '$', '#', '@']

def is_numeric(ele):
    try:
        float(ele)
        return True
    except:
        return False

with open('Program 1.txt') as f:
    data = f.read()
    tokens = data.split()

    for index, ele in enumerate(tokens):

        if ele in keywords:
            print(ele, "is a keyword") # int
        elif ele in operators:
            print(ele, "is an operator") # +
        elif ele in special_char:
            print(ele, "is a special character") # ;
        elif is_numeric(ele):
            print(ele, "is a constant") # 3.14
        elif index > 0 and tokens[index-1] == "=":
            print(ele, "is a literal") #
        else:
            print(ele, "is an identifier")



# values that are directly specified in the code are literals 
# EG: int a = 10;
#     char c = "spcc"

# however we further classify 10 as a constant

# 10 = literal, constant
# spcc = literal
# a = identifierr