s=input()
new=" "
count=0
for i in s:
    if(i=="-"):
        count+=1
    else:
        new+=i    
print("-"*count+new)            