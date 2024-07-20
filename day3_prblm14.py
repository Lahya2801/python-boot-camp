#find the missing number in array
#1 2 3 4 6 7 8 9 10
my_list=list(map(int,input().split(" ")))
k=sum(my_list)
print("sum of list:",k) 
sum=0
n=int(input("Enter the number"))
sum=(n*(n+1))//2
#for i in range(1,n+1):
   #sum+=i
print(f"the sum of first {n} natural numbers is",sum)
print("missing number in the list is:",sum-k)
