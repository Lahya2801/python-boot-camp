a= int(input("enter the 1st side:"))
b=int(input("enter the 2nd side:"))
c=int(input("enter the 3rd side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of the trangle is :",area)