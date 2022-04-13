def sum():
    n=5674
    result=0
    while n>0 or result>9:
        if n==0:
            n=result
            result=0
        l=n%10
        result+=l
        n=n//10
    return result
ass=sum()
print(ass)