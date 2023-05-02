from prettytable import PrettyTable
x = PrettyTable()

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

x.field_names = ["Token", "Token Category"]
token_row = []

with open('Lab 2\Program 1.txt') as f:
    data = f.read()
    tokens = data.split()

    for index, ele in enumerate(tokens):
        token_row.append(ele)

        if ele in keywords:
            token_row.append("Operator")
        elif ele in special_char:
            token_row.append("Special Character")
        elif is_numeric(ele):
            token_row.append("Constant")
        elif index > 0 and tokens[index-1] == "=":
            token_row.append("Literal")
        else:
            token_row.append("Identifier")

        x.add_row(token_row)
        token_row = []

print(x)