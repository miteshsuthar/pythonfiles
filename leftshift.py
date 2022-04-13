def leftshift(ar):
    x=ar[0]
    l=len(ar)
    for i in range(1,l):
        ar[i-1]=ar[i]
    ar[-1]=x

ar=[5,10,15,20,25,18,7]
print(ar)
k=int(input("Enter the no. how many number are you shift in the list "))
for j in range(k):
    leftshift(ar)
print(ar)