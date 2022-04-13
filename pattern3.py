n=int(input())
count=1
for i in range(1,(n//2)+1):
    for j in range(i):
        if count<=n:
            print(count,end=' ')
            count+=1 
    print()