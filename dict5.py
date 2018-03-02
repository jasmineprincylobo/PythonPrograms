"""Add name and salary {name:salary} for n number of
employees through keyboard in a dictionary and print
only the employees whose salary is greater than 2000 but less than 4000"""

n=int(input("Enter no of records"))
d={}
for i in range(1,n+1):
    name=input("Enter name: %d"%(i))
    sal=int(input("Enter sal: %d"%(i)))
    d[name]=sal
print({j:d[j] for j in d if d[j]>2000 and d[j]<4000})
