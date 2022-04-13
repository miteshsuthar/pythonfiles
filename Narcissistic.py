n=int(input())
num=n
lnth=len(str(n))

sum=0
while n>0:
    l=n%10
    sum=sum+pow(l,lnth)
    n=n//10

if num==sum:
    print('Yes')
else:
    print('No')
