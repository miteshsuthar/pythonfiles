def chocalate_distributer(arr,m,n):
    min=9999
    arr.sort()
    for i in range(0,m-1):
        max_diff=arr[i+m-1]-arr[i]
        if max_diff<min:
            min=max_diff
    return min
# arr =[3,4,1,9,56,7,9,12]
arr=[7,3,2,4,9,12,56]
m=3
n=len(arr)
print(chocalate_distributer(arr,m,n))

