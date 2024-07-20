#print the element in a particular index using cyclic printing.
my_list=list(map(int,input().split(" ")))                       
k=int(input())
#for i in range(0,len(my_list)):
   #if(i==k):
    #print(my_list[k])
    #break
#if(k>len(my_list)):                                            #input=2 3 4 5 6
n=k%(len(my_list))                                              #0 1 2 3 4
      #n=k-len(my_list)                                               k=8,then index= 8%5=3----> o/p=5
print(my_list[n])
     

          