arr=[3,6,9,13]
count=0
n=3
size=3
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if (arr[i]+arr[j]+arr[k])%size==0:
                count+=1
print(count)
