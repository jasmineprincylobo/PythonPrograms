#4. Write a program for finding surface areas of cylinder and cone (2*PI*r*r*h, 1/3*PI*r*r*h) using function.
import math
def Cyl(r,h):
 val= 2*3.14*r*r*h  
 return val
def Cone(r,h):
 val2= 1/3*3.14*r*r*h 
 return val2
print("S. A of cylinder:",Cyl(5,8))
print("S. A of cone:",Cone(5,8))

