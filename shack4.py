n=int(input(''))
a=1
b=1
fib=0
for i in range(n-2):
    fib=b+a
    b=a
    a=fib
    if n==1 or n==2:
        print(1)  
        break
print(fib)