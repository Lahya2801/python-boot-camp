#write a code to print all the capital letter in astring
s=input()
count=" "
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        count+=i
print(count)        
    