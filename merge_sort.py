def merge_sort(arr,start,end):
    if start<end:
        mid=(start+end)//2
        merge_sort(arr,start,mid)
        merge_sort(arr,mid+1,end)
        merge(arr,mid,start,end)


def merge(arr,mid,start,end):
    i=start
    j=mid+1
    k=start
    result=[0]*(end+1)
    while i<=mid and j<=end:
        if arr[i]<arr[j]:
            result[k]=arr[i]
            k+=1
            i+=1
        else:
            result[k]=arr[j]
            k+=1
            j+=1
    while i<=mid:
        result[k]=arr[i]
        k+=1
        i+=1
    while j<=end:
        result[k]=arr[j]
        k+=1
        j+=1
    for p in range(start,end+1):
        arr[p]=result[p]

arr=[30,20,10,40,80,70,60]
start=0
end=len(arr)-1
merge_sort(arr,start,end)
print(arr)
