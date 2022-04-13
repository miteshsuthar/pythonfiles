arr=[5,4,-3,2,-5,3]
n=len(arr)
count=0
for i in range(n):
    for j in range(n):
        if -arr[i]==arr[j]:
            if arr[i]>0:
                print(arr[i],end=' ')
                print(arr[j])
                count=1
    if count==0:
        print("doesn't present any pair ")        