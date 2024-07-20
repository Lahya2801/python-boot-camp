#find the   duplicates in an array
#8 7 7 8 5 4 4 8 9


my_list=list(map(int,input().split(" ")))
new_list=[]
for i in range(len(my_list)):
    if(my_list[i] not in new_list):
        new_list.append(my_list[i])
       
print(new_list)        

