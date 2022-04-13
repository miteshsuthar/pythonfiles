def sum(arr,start,end):
    sum=0
    for i in range(start,end+1):
        sum = sum+arr[i]
    return sum


    for i in range(1,n-1):
        ls=sum(arr,0,i-1)
        rs=sum(arr,i+1,n-1)
        if ls==rs:
            return arr[i]
        return -1
arr=[2,3,4,1,4,5]
start=0
end=0
result=sum(arr,start,end)
print(result)

