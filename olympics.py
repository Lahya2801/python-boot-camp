''''''''''
Mr.Z is  select for Olympics .He is participating in swimming competition, only one winner is selected among all participates
and X and Y are friends of Z . X is participate in badminton, Y in table tennis. According to the selection committee  requirements for badminton
1. height=140 cm
2.weight= factors of 2
3.body fat <12%
       
 According to the selection for table tennis are
1 height=118 -148
2. weight= factors of no. of medals won by Mr.Z
3. body fat=14%

According to the previous history Z participated in 14 games out of this he is having success rate of 50%.
write a program  to check whether Z,X,Y travel in same plane or not.

'''''''''

bh=int(input("height of X"))
bw=int(input("weight of X"))
th=int(input("height of Y"))
tw=int(input("weight of Y"))
fact7=(50*14)/100 
if(bh==140 and bw%2==0):
    print("Mr.X are selected for batminton")
elif(th<140 and th>118 and tw%fact7==0):
    print("Mr.Y are selected for table tennis")
else:
    print("Mr.Z are selected for swimming")         