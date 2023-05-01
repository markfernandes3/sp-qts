# E -> TE'
# E'-> +TE'|e
# T -> FT'
# T'-> *FT'|e
# F -> (E) |id
# input d+d*d
# input d+d*

def E(Str, l):
    l = T(Str, l)
    l = Ed(Str, l)
    return l

def T(Str, l):
    l = F(Str, l)
    l = Td(Str, l)
    return l

def Ed(Str, l):
    if Str[l[0]] == "+":
        l[0] += 1
        l = T(Str, l)
        l = Ed(Str, l)
    return l

def F(Str, l):
    if Str[l[0]] == "(":
        l[0] += 1
        l = E(Str, l)
        if Str[l[0]] == ")":
            l[0] += 1
        else:
            l = error(l)
    elif Str[l[0]] == 'd':
        l[0] += 1
    else:
        error(l)
    return l

def Td(Str, l):
    if Str[l[0]] == "*":
        l[0] += 1
        l = F(Str, l)
        l = Td(Str, l)
    return l

def error(l):
    print ("Error occured!")
    l[1] = 1
    return l

input = input("Enter a string: ") + "$"
l = [0, 0]
l = E(input, l)

if l[1] == 0:
    print ("String is Valid")
else:
    print ("String is invalid")
