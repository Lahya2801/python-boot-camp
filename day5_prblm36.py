#home work very important

s=input()
n=int(input())
s1=s.upper()
for i in s1:
       new=ord(i)+n
       print(chr(new),end=" ")  
    
if(new>90):
       k=new%len(s)
       new=k-n
       print(chr(new),end=" ")