# password verifier 
# Mr.X is trying to create a new password for his instagram account. these are the required conditions for create any new password
#1.minimum length is 8 ,max length is 15
#2.only @,/  are allowed in a password
#3.No spaces are allowed
#4.only alphanumerics are allowed
# U R suppose to print weak if length is exact 8  , medium length is b/t 8 to 12, strong if length is b/t 12 to 15 
s=input()
n=len(s)
count=0
str="@/"
for i in s:
 if(i==str[0] or i==str[1]):
        count+=1     
        break
if(count==0):       
   print("please follow the conditions")
elif(n<8):
   print("please follow the conditions")
elif(n==8):
    print("password is weak")   
elif(n>8 and n<12):
    print("password is moderate")
elif(n>=12 and n<15):
    print("password is strong")    
else:
    print("very strong")   
