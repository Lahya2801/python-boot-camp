my_list=list(map(int,input().split(",")))
print("choose 1 for append\n 2 for pop\n 3 for sort\n 4 for length")
choice=int(input("enter the choice:"))
if(choice==1):
  my_list.append(6)
  print(*my_list)
elif(choice==2):
  my_list.pop(3)
  print(*my_list)
elif(choice==3):
  my_list.sort()
  print(*my_list)  
else:
  print(len(my_list))