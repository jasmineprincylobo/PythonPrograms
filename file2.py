#Program to count the occurrences of a letter in a text file.

c=0
fname = input("Enter file name: ")
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i.isspace):
               c+=1
        print(c)

