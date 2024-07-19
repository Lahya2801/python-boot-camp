my_list=list(map(int,input().split(" ")))
even=0
odd=0
for i in range(len(my_list)):
    if(my_list[i]%2==0):
        even+=1
    
    else:
        odd+=1
print(f"{odd} no.of odd elements")
print(f"{even} no.of even elements")
      
