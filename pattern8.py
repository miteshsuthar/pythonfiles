n=int(input("this is my input"))
for i in range(1,n+1):
    x=1
    flag=0
    print("  "*(n-i),end=' ')
    for j in range(1,2*i):
        print( x ,end=' ')
        if flag==0:
            x+=1
        else:
            x-=1
        if x==i:
            flag=1
    print()


