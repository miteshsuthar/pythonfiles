n=int(input())
for i in range(n):
    flag=n-1
    count=i+1
    for j in range(i+1):
        print(count,end=' ')
        count=count+flag
        flag=flag-1     
    print()