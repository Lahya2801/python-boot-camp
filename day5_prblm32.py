#print the reverse order of numeric in alphanumeric string
s=input()
nums="0123456789"
ans=""
for i in s:
    if(i in nums):
        ans+=i
ans=int(ans)
while(ans>0):
    r=ans%10
    ans=ans//10
    print(r,end="")    
