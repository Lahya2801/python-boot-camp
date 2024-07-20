#find the element   present in (k+N)th index.k is given by user.
my_list=list(map(int,input().split(" ")))
k=int(input())
N=int(input())
leng=len(my_list)
if(leng<k+N):
    print("ERROR")
else: 
    for i in range(len(my_list)):
       print(my_list[k+N],end=" ")
       break        
    #for i in range(leng):
       #if(i==k+N): 
        #print("the element present in the (k+N)th position is:",my_list[i])  



