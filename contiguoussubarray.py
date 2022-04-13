ar=[1,2,3,-2,5]
n=len(ar)
sum=0
l1=[]
for i in range(n):
    sum=sum+ar[i]
    l1.append(sum)
sum=0
for i in range(-1,-(n+1),-1):
    sum=sum+ar[i]
    l1.append(sum)
l=max(l1)
print(l)