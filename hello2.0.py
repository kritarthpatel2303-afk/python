n=int(input("enter number of elements"))
a=0
b=1
print("fibbonacci series is :")
for i in range (n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
