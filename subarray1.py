def sumsubarray(ar,ar1,n):
   
    for i in range(n):
        sum=0
        j=1
        while j<n:
            if sum==0:
                sum=sum+ar[i]+ar[j]
                j+=1
            else:
                sum=sum+ar[j]
                j+=1
        ar1.append(sum)
    
# ar=[4,2,0,1,6]
ar=[4,-2,-3,-1,6]
ar1=[]
n=len(ar)
sumsubarray(ar,ar1,n)
print(ar1)
s=max(ar1)
print(s)