def merge_sort(arr,low,high):
    if low<high:
        mid =(low+high)/2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,mid,high,low)

def merge(arr,mid,high,low):
    i=low
    k=low
    j=mid+1
    temp=[]
    while i<=mid and j<=high:
        if arr[i]<arr[j]:
            temp[k]=arr[i]
            i+=1
            k+=1
        else:
            temp[k]=arr[j]
            j+=1
            k+=1
    while i<=mid:
        temp[k]=arr[i]
        i+=1
        k+=1
    while j<=high:
        temp[k]=arr[j]
        j+=1
        k+=1
    for p in range(low,high+1):
        temp[p]=temp[k]
        print(temp[p])
arr=[12,34,2,4,12,32]
low=0
high=len(arr)-1
merge_sort(arr,low,high)

