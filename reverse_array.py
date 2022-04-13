def reverse_K(ar,n):
    k=3
    for i in range(k-1,-1,-1):
        ar1.append(ar[i])
    for j in range(n-1,k-1,-1):
        ar1.append(ar[j])
    return ar1
ar=[1,2,3,4,5,6,7]
n=len(ar)
ar1=[]
result=reverse_K(ar,n)
print(result)
