n=int(input())
a=1
b=1
fib=0
l1=[]
l1.append(1)
l1.append(1)
for i in range(n):
    fib=a+b
    b=a
    a=fib
    l1.append(fib)
print(l1)
for i in range(n):
    if i==n-1:
        print(l1[i])
        break