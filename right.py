def rightshift(ar):
    l=len(ar)
    x=ar[l-1]
    for i in range(l-2,-1,-1):
        ar[i+1]=ar[i]
    ar[0]=x
ar=[5,10,15,20,25,18,7]
print(ar)
k=int(input("Enter the no. how many number are you shift in the list "))
for j in range(k):
    rightshift(ar)
print(ar)