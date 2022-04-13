n=int(input())
for i in range(1,n+1):
    x=1
    print(" "*(n-i),end=' ')
    for j in range(1,i+1):
        if j==1 or i==n or j==i:
            print( x ,end=' ')
        else:
            print(" ",end=' ')
        x+=1
    print()