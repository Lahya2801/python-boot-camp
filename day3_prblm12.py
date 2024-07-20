my_list=list(map(int,input().split(" ")))
min=0
for i in range(len(my_list)):
    if(min>my_list[i]):
        min=my_list[i]
print("the minimum element in the list is:",min)
    