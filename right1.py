def rightshift(ar):
    l=len(ar)
    x=ar[l-1]
    for i in range(l-2,-1,-1):
        ar[i+1]=ar[i]
    ar[0]=x
ar=[5,10,15,20,25,18,7]
print(ar)
rightshift(ar)
print(ar)
ar=[1,3,5,2,4,7,9]
print(ar)
rightshift(ar)
print(ar)
