#find the maximum element in a given list.
my_list=list(map(int,input().split(" ")))
max=0
for i in range(len(my_list)):
    if(max<my_list[i]):
        max=my_list[i]
print("the maximum element in the list is:",max)
    
            
