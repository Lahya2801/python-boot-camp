#sum of numeric in the given string using ASCII values
s=input()
sum=0
for i in s:
    if(ord(i)>=48 and ord(i)<=57):
        sum+=int(i)
print(sum)        
    