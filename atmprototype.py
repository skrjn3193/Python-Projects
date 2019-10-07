import datetime
acc1=[61215934035,1122,"06/06/2018",1800]
acc2=[61215934036,2211,"07/06/2018",2200]
acc3=[61215934037,1234,"08/06/2018",2800]
print("Hello How may i help you \n")
pin=int(input("enter your 4 digit pin \n"))
def account1():
    choice=int(input(" what do u want to do \n 1.Deposit \n 2.Widhrawl \n 3.Balance Inquiry \n 4.Last transaction "))
    if(choice==1):
        cash=int(input("how many u want to deposit"))
        acc1[3]+=cash
        acc1[2]=datetime.date.today()
    elif(choice==2):
        out=int(input("how many you want to withdraw"))
        acc1[3]=acc1[3]-int(out)
        acc1[2]=datetime.date.today()
        print("your balance is", acc1[3])
    elif(choice==3):
        print("your current balance is ",acc1[3])
    elif(choice==4):
        print(" last transaction date is",acc1[2])
        
    else:
        print("wrong choice")
def account2():
    choice=int(input(" what do u want to do \n 1.Deposit \n 2.Widhrawl \n 3.Balance Inquiry \n 4.Last transaction "))
    if(choice==1):
        cash=int(input("how many u want to deposit"))
        acc2[3]+=cash
        acc2[2]=datetime.date.today()
    elif(choice==2):
        out=int(input("how many you want to withdraw"))
        acc2[3]=acc2[3]-out
        acc2[2]=datetime.date.today()
        print("your balance is", acc2[3])
    elif(choice==3):
        print("your current balance is ",acc2[3])
    elif(choice==4):
        print(" last transaction date is",acc2[2])
        
    else:
        print("wrong choice")
def account3():
    x=1
    while(x!=0):
        choice=int(input(" what do u want to do \n 1.Deposit \n 2.Widhrawl \n 3.Balance Inquiry \n 4.Last transaction "))
        if(choice==1):
            cash=int(input("how many u want to deposit"))
            acc3[3]+=cash
            acc3[2]=datetime.date.today()
        elif(choice==2):
            out=int(input("how many you want to withdraw"))
            acc3[3]=acc3[3]-out
            acc3[2]=datetime.date.today()
            print("your balance is", acc3[3])
        elif(choice==3):
            print("your current balance is ",acc3[3])
        elif(choice==4):
            print(" last transaction date is",acc3[2])
        
        else:
            print("wrong choice")
        x=int(input("do u wish to continue \n 1. Yes \n 0. No "))
        
if(pin==acc1[1]):
    account1()
elif(pin==acc2[1]):
    account2()
elif(pin==acc3[1]):
    account3()
else:
    print("you entered wrong pin")

    
