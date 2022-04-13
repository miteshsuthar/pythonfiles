arr=[1,2,3,4,5]
n=len(arr)
l=[]
sum=0
for i in range(n):
    sum=sum+arr[i]
    l.append(sum)
sum=0
for i in range(-1,-(n+1),-1):
    sum+=arr[i]
    l.append(sum)
    m=max(l)
print(m)