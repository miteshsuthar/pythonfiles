def reverse(n,s):
    if n>0:
        s=s*10+n%10
        reverse(n//10,s)
    else:
        return s  
n=int(input())
s=0
print(reverse(n,0))