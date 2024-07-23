#GCD of two numbers
'''''''''

a=int(input())
b=int(input())
while b!=0:
    a,b=b,a%b
print("GCD of 2 numbers is:",a)
'''''''''

a=int(input())
b=int(input())
mul=a*b
while b!=0:
    a,b=b,a%b
print("GCD of 2 numbers is:",a)
print("LCM of 2 numbers is:",mul/a)