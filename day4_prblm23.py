n=int(input())
count=0
r=n**0.5
for  i in range(2,int(r+1)):
    if(n%i==0):
        count+=1
        break
if(count==0):
    print(f"{n} prime number") 
else:
    print(f"{n} is not prime number")           
