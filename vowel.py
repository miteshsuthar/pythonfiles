def leftshift(ar):
    l=len(ar)
    x=ar[l-1]
    print(x)
    for i in range(l-2,-1,-1):
        ar[i+1]=ar[i]
    ar[0]=x
ar=[3,4,8,2,1,12,10]
print(ar)
leftshift(ar)
print(ar)
k=int(input("Enter the no. how many number are you shift in the list "))
for j in range(k):
    leftshift(ar)
print(ar)