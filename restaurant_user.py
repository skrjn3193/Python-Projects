import xlrd
data=xlrd.open_workbook("restaurant.xls")
table=data.sheet_by_index(0)
a=table.col_values(0)
b=table.row_values(0)
print(" Our Menu is :  \n ")
for j in range(0,len(a)):
    print(table.row_values(j))
item_no=table.col_values(0)
print(item_no)
item_name=table.col_values(1)
item_price=table.col_values(2)
x=1
bill=0
while(x!=0):
    choice=int(input("enter your choice to order , Please select item number \n"))
    print(item_no)
    if choice in item_no:
        index=item_no.index(choice)
        quantity=int(input("enter quantity"))
        bill+=item_price[index]*quantity
        x=int(input("do u want to add more \n 1-Yes \n 0-No "))
    else:
        print("You entered wrong choice,Please Check it again")
print("Your total bill is : ", bill) 
