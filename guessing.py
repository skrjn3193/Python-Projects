import random
a=[0,0,0,0,0]
user=0
computer=0
for i in range(5):
    a[i]=random.randint(1,10)
n=int(input("How many times you want to guess "))
for j in range(n):
    b=int(input("Guess 1st number of list between 1 to 10"))
    if(b==a[0]):
        user+=1
        print("Your answer is correct \n")
        print("List was",a)
        random.shuffle(a)
    else:
        computer+=1
        print("Your answer is wrong \n")
print("Your score = ",user)
print("Computer score = ",computer)

            
    
