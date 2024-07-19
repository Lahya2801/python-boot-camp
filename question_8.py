my_list=list(map(int,input().split(" ")))
count=0
sum=0
avg=0
for i in range(len(my_list)):
    #if(i%2==0):
     #print(my_list[i])
     count+=1   
     sum+=my_list[i]  
     avg=sum/count
print(f"{avg}  is average of all even numbers in the given list")
