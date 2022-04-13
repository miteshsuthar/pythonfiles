n=5
ar=[1,2,3,-2,5]
ar1=[]
sum=0
s=0
i=0
while i<n+1:
    sum=sum+ar[i]
    i+=1
    if i==n:
        s+=1
        i+=1
        ar1.append(sum)
        print(ar1)
        if s==n-1:
            print(s)
            break
print(ar1)
        




