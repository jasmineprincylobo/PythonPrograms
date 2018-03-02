#6. Write a Calculator program to find arithmetic operations ( +,-,*,/ and %) using functions for two nos with  menu choice
loop=1
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
print("calculator")
n1=int(input("enter num1:"))
n2=int(input("enter num2:"))
while(loop==1):
    ch=int(input("enter ur choice:"))

    if(ch==1):
        print("sum:",sum(n1,n2))
    elif(ch==2):
        print("sub:",sub(n1,n2))
    elif(ch==3):
        print("mul:",mul(n1,n2))
    elif(ch==4):
        print("div:",div(n1,n2))
    elif(ch==5):
        print("mod:",mod(n1,n2))
    else:
            loop=0
            #exit(0)
print("Good Bye")
        
        
   

