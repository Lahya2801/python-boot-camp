#print the unique characters in a string

s=input()
ans=""
for i in s:
    if(i not in ans):
        ans+=i
print(ans)        

    