#greater of two nos
def great(a,b):
    if a>b:
        return a
    else:
        return b
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
print("Greater num = ",great(a,b))
