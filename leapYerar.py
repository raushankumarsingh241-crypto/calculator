yer=int(input("enter a year:"))
if  yer%400==0:
    print(f"given year {yer} is leap year ")
elif yer%4==0 and yer%100!=0:
    print(f"given year {yer} is leap year ")
else:
    print(f"given year {yer} is not a leap year")
