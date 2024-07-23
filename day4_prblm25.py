#leap year
'''''''''
year=int(input())
if(year%4==0 and year%100!=0):
    print(f"given {year} is leap year")
else:
    print(f"{year} is not a leap year")    

'''''''''


for i in range(2000,2025):
    if((i%4==0) and (i%100!=0)) or (i%400==0):
        print("leap year",i)
    else:
        print("not leap year",i)  

