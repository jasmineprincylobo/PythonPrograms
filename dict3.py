"""Add  name and salary {name:salary} for n number of employees through
keyboard in a dictionary and print them in
name alphabetical order with salary"""
n=int(input("Enter no of records"))
d={}
for i in range(1,n+1):
    name=input("Enter name %d"%(i))
    sal=int(input("Enter mark %d"%(i)))
    d[name]=sal
    #d.sort()
    print (d)
