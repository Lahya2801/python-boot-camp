#remove all the brackets from the given algebric expression
'''''''''
s=input()
for i in s:
   if(i!=chr(40) and i!=chr(41) and i!=chr(123) and i!=chr(125) and i!=chr(93) and i!=chr(91)):
    print(i,end=" ")
      
'''''''''


s=input()
for i in s:
    if(ord(i)==40 or ord(i)==41 or ord(i)==123 or ord(i)==125 or ord(i)==91 or ord(i)==93):
        pass
    else:
        print(i,end=" ")
     