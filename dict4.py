


#Add  name and salary {name:salary} for n number of employees through keyboard
#in a dictionary and print the sum,max, min and average of the salaries

n=int(input("Enter no of records"))
d={}
for i in range(1,n+1):
    name=input("Enter name: %d"%(i))
    sal=int(input("Enter sal: %d"%(i)))
    d[name]=sal
    #d.sort()
   # print("sum:"(sum(d.values())))
    print (d)
    print(sum(d.values()))
    print(max(d.values()))
    print(min(d.values()))
