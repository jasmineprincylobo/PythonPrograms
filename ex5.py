a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
c=int(input("enter 3rd num:"))
d=int(input("enter 4th num:"))
def greatestOfFour(a,b,c,d):
    if(a>b and a>c and a>d):
      return (a)
    elif(b>c and b>d):
         return(b)
    elif(c>d):
         return(c)
    else:
       return(d)
print("Greatest number:",greatestOfFour(a,b,c,d))
         
