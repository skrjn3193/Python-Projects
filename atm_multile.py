r=0;j=100
amt=[1000,2000,3000,4000]
u=['1234','4321','5678','9999']
while(r<3):
    a=input('enter your pin')
    for i in range (0,len(u)):
        if(a==u[i]):
            j=i
            break
    if(j==i):
        print('you are welcome')
        q=int(input('wht do u want to perform 1>withdraw 2>deposit 3>cancel'))
        if(q==1):
            t=int(input('enter your amount'))
            print('your balance is')
            print(amt[j])
            if(t<=amt[j]):
                result=amt[j]-t
                print('your balance is')
                print(result)
                break
        if(q==2):
            t=int(input('enter your amount'))
            result=amt[j]+t
            print('your balance is')
            print(result)
            break
        if(q==3):
            r=5
        else:
            print('enter again')
            r=r+1
            
            
    else:
        print('enter again')
        r=r+1
if(r==3):
    print('blocked')
    
        
    
    
    
