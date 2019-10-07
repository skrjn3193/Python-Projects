import xlwt
import random
workbook=xlwt.Workbook()
table=workbook.add_sheet("Menu")
table.write(0,0,"Item no.")
table.write(0,1,"Item Name")
table.write(0,2,"Item Price")
for i in range(1,10):
    table.write(i,0,str(i))
for j in range(1,10):
    table.write(j,1,input("enter item name"))
    table.write(j,2,input("enter price of the item"))
workbook.save("restaurant.xls")
