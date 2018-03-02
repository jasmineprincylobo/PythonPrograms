def primeno(a):
    if (a==1):
        return False
    elif (a==2):
        return True;
    else:
        for x in range(2,a):
            if(a % x==0):
                return False
        return True
def factorial(a):
    fact=1
    while(a>0):
        fact=fact*a
        a-=1
    return fact
def palindrome(a):
    for i in range(int(len(a)/2)): 
        if a[i] != a[len(a)-i-1]:
            return False
    return True
def OddorEven(a):
    if (a % 2) == 0:
        return "Even"
    else:
        return "Odd"
