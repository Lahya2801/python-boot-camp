#print all the vowels followed by consonents in a given string    
vowel="aeiou"
con="bcdfghjklmnpqrstvwxyz"
ct_c=""
ct_v=""
s=input()
new=s.lower()
for i in new:
    if(i in vowel):
        if(i not in ct_v):
          ct_v+=i
for i in new:
     if(i in con):
         if(i not in ct_c):
            ct_c+=i  
ans=ct_v+ct_c         
print(ans)