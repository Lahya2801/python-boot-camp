#check how many vowels are in a string
'''''''''
s=input()
count=0
inp=s.lower()
vowel="aeiou"                                                  #for cosonants count
for i in inp:                                                    #if(i not in vowel):
    if(i in vowel):
        count+=1
print(count)        

'''''''''


vowel="aeiou"
con="bcdfghjklmnpqrstvwxyz"
ct_c=0
ct_v=0
s=input()
new=s.lower()
for i in new:
    if(i in vowel):
        ct_v+=1
for i in new:
     if(i in con):
         ct_c+=1    
print("the vowel count of the given string is:",ct_v)
print("the consonent count of the given string is:",ct_c)                 