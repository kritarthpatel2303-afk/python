year=int(input("enter year :"))
if(year%4==0 and year%400==0 ):
         print("this year is leap year",year)
else:
    print("this is not a leap year")
