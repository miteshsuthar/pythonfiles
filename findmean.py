def findmin(arr):
    sum=0
    minvalue=0
    for i in arr:
        sum=sum+i
        if sum<minvalue:
            minvalue=sum
    return (1-minvalue)
# arr=[-3,2,-3,4,2]
arr=[1,2]
result= findmin(arr)
print(result)
