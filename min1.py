# arr=[-3,2,-3,4,2]
arr=[1,2]
n=len(arr)
min_ele=0
min_val=0
for i in range(n):
    min_ele=min_ele+arr[i]
    min_val=min(min_val,min_ele)
result=1-min_val
print(result)
