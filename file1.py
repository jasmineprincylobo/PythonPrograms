#Program to count the occurrences of a letter in a text file.


fname = input("Enter file name: ")
let=input("Enter letter to be searched:")
k = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for j in i:
             if(j==let):
                k=k+1
print("Occurrences of the characters:")
print(k)
