#replace the elemens in a array with average of maximum and minimum element
# sample   i/p   13 2 67 20 68
# o/p   max=68  ,min=2  ,avreage=35
#output = 35 35 35 35 35

my_list=list(map(int,input().split(" ")))
max=0
min=my_list[0]
for i in range(len(my_list)):
    if(max<my_list[i]):
        max=my_list[i]  
print(max)        
for i in range(len(my_list)):
    if(min>my_list[i]):
        min=my_list[i] 
print(min)         
avg=(max+min)//2
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)
 