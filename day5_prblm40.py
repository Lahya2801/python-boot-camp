'''''''''
r=int(input( ))
c=int(input())
for i in range(r):
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(c):
        print("*",end=" ")
    print()       
''''''''' 


r=int(input( ))
c=int(input())
for i in range(r):
    for j in range(c+i):
        if(j<i):
         print(" ",end=" ")
        else:       
            print("*",end=" ")
    print()       