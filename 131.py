x1=int(input("enter x1 : "))
x2=int(input("enter x2 : "))
x3=int(input("enter x3 : "))
y1=int(input("enter y1 : "))
y2=int(input("enter y2 : "))
y3=int(input("enter y3 : "))
x=(y2-y1)/(x2-x1)
y=(y3-y1)/(x3-x1)
z=(y3-y2)/(x3-x2)
if(x==y and y==z and x==z):
    print("All points are on same line")
else:
    print("All points are not on same line")




