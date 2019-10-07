import xlrd
import xlwt
import datetime
import random
import time
#import RPi.GPIO as io
#import serial


#io.setwarnings(False)
#io.setmode(io.BOARD)
#io.setup(13,io.IN)
#io.setup(7,io.IN)


workbook=xlwt.Workbook()
table=workbook.add_sheet("Data of vehicles")
table.write(0,0,"Your name")
table.write(0,1,"your tag no")
table.write(0,2,"entry time")
workbook.save("Vehicles_data.xls")
vehicles=[]
i=0
count=0

def writedata(count):
    table.write(count,0,input("your name please"))
    n=int(input("enter card number"))
    table.write(count,1,n)
    vehicles.append(int(n))
    start_time=datetime.datetime.now()
    table.write(count,2,start_time)
    workbook.save("Vehicles_data.xls")
    
    print("Your payment is successful")
    print("open the gates")
    return vehicles

"""def writedata(count):
    table.write(count,0,input("your name please"))
    print("Punch your rfid")
    ser=serial.Serial('/dev/ttyUSB)',9600)
    rf1=ser.read(12)
    print(rf1)
    table.write(count,1,rf1)
    vehicles.append(int(rf1))
    print(datetime.datetime.now())
    table.write(count,2,start_time)
    workbook.save("Vehicles_data.xls")
    
    print("Your payment is successful")
    print("barrier is open for next 20 seconds")
    time.sleep(.2)
    print("barrier ")
    return vehicles
"""

def checkdata():
    tag_nos=[]
    t=[]
    data=xlrd.open_workbook("Vehicles_data.xls")
    record=data.sheet_by_index(0)
    tag_nos=record.col_values(1)
    print(tag_nos)
    t=record.col_values(2)
    print(t)
    cardno=int(input("your card no"))
    if cardno in tag_nos:
        skr=tag_nos.index(cardno)
        print("Barrier opened , you may go now")
        """
        logouttime=datetime.datetime.now()
        totaltime=logouttime-logintime
        if(totaltime<24):
            print("your data is matched and you can go")
        else:
            print("You are late , please pay more money to go")
            writedata(count)
        """
    else:
        writedata(count)

"""def checkdata():
    tag_nos=[]
    data=xlrd.open_workbook("Vehicles_data.xls")
    record=data.sheet_by_index(0)
    tag_nos=record.col_values(1)
    #print(tag_nos)
    t=record.col_values(2)
    #print(t)
    print("punch your card")
    ser=ser.Serial('/dev/tty/USB0',9600)
    cardno=ser.read(12)
    if cardno in tag_nos:
        skr=tag_nos.index(cardno)
        print("You are already registered, you can go now")
        print("Barrier opened , you may go now")
        
        logouttime=datetime.datetime.now()
        totaltime=logouttime-logintime
        if(totaltime<24):
            print("your data is matched and you can go")
        else:
            print("You are late , please pay more money to go")
            writedata(count)
        
    else:
        
        writedata(count)
"""       

while(1):
    print("\n Car :60 \t Bus/Truck :100 \t Loaded Vehicles :200")
    ##i=int(input("enter value of i"))
    if(io.input(13)):
        print("car arriving")
        count=count+1
        writedata(count)
        
    elif(io.input(7)):
        checkdata()
        print("car returning")

        
