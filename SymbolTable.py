from random import random

class Symboltable:
    def __init__(self,expression):
        self.expression = expression
        self.table = []
        
    def insertsymboltable(self,newsymbol):
        row = []
        if newsymbol.isalpha():
            row.append(newsymbol)
            row.append("identifier")
        else:
            row.append(newsymbol)
            row.append("operator")
        row.append(random()*10**8)
        self.table.append(row)
            
    def removesymbol(self,out_symbol):
        for i in self.table:
            if out_symbol == i[0]:
                self.table.remove(i)
        self.tablebuilder()

    def searchsymbol(self,key_symbol):
        for i in self.table:
            if key_symbol == i[0]:
                print("{} \t {} \t {:.0f}".format(i[0],i[1],i[2]))

    def createsymboltable(self):
        temp_row = [i for i in self.expression.split(' ')]
        for i in temp_row:
            self.insertsymboltable(i)

    def tablebuilder(self):
        print("Symbol \t Type \t\t Location")
        for i in self.table:
            print("{} \t {} \t {:.0f}".format(i[0],i[1],i[2]))
            
            
tablelist = []
while True:
    x = int(input("Choose the operation to be performed\n\t 1:Create Symbol Table \n\t 2:Add Elements to the table \n\t 3:Remove elements from the table \n\t 4:Search for elements from the table \n\t 5:Diplay specific table \n\t 6:Display all tables \n\t Press anything else to exit \n"))
    if x == 1:
        expression = input("Enter expression split acording to space:\n")
        a = Symboltable(expression)
        a.createsymboltable()
        tablelist.append(a)
        for i in range(len(tablelist)):
            print("Table Id : ",i)
            tablelist[i].tablebuilder()
    elif x == 2:
        table_id = int(input("Enter the Table id of the table on which operation is to be performed:\n"))
        tablelist[table_id].insertsymboltable(input("Enter the symbol  to be added:\n"))
        tablelist[table_id].tablebuilder()
    elif x == 3:
        table_id = int(input("Enter the Table id of the table on which operation is to be performed:\n"))
        tablelist[table_id].removesymbol(input("Enter the symbol to be removed:\n"))
    elif x == 4:
        table_id = int(input("Enter the Table id of the table on which operation is to be performed:\n"))
        tablelist[table_id].searchsymbol(input("Enter input to be searched:"))
        tablelist[table_id].tablebuilder()
    elif x == 5:
        table_id = int(input("Enter the Table id of the table on which operation is to be performed:\n"))
        tablelist[table_id].tablebuilder()
    elif x == 6:
        i=0
        for j in tablelist:
            tablelist[i].tablebuilder()
            i=i+1
    else:
        break