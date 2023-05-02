import random

while(True):
    print("")
    choice=input("1.Create Table    2.Search Table      3.Enter Symbol      4.Remove Symbol     5.View Table        6.Exit\nEnter Your Choice: ");  
        
    if(choice=="1"):
        expression=input("Enter Expression: ")
        expression = expression.replace(' ', '') # removing spaces form the expression


    elif(choice =="2"):
        symbol=input("Enter Symbol to search: ")
        print("Symbol: ",symbol,"|Address: ",random.randint(1000,9999),"|Type: ",symbol_type(symbol))

    elif(choice == "3"):
        symbol = input("Enter Symbol: ")
        expression += symbol

    elif(choice == "4"):
        symbol = input("Enter Symbol to remove: ")
        expression=expression.replace(symbol,'')

    elif(choice == "5"):
        for symbol in expression:
            print("Symbol: ", symbol, "|Address: ", random.randint(1000,9999), "|Type: ",symbol_type(symbol))
    elif(choice == "6"):
        break
            
    def symbol_type(symbol):
        if(symbol.isalpha() or symbol.isnumeric()):
            return"identifier"
        else:
            return "operator"