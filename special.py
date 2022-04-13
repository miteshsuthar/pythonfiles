n=int(input())
s=str(n)
num=len(s)
mul=0
for i in s:
    n1=int(i)
    mul=mul+n1*n1*n1
p=str(mul)
if n==mul:
    print(len(s)+1)




