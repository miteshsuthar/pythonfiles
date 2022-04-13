def sum(arr,n):
    sum=0
    for i in range(n):
        for j in range(n):
            if -arr[i]==arr[j]:
                if arr[i]>0:
                    sum=sum+arr[i]
                else:
                    sum=sum-arr[i]
                break
        if j==n-1:
            sum=sum+arr[i]
            
arr=[-5,4,3,-4,5,-8]
n=len(arr)
result=sum(arr,n)
print(result)                

