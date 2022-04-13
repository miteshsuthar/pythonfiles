def subarray(ar,n):
    s=set(ar)
    sum=0
    for i in ar:
        sum=sum+i
        if sum in s or sum==0:
            return False
    return True 
# ar=[7,2,0,1,8]
ar=[4,2,-3,1,6]
# ar=[4,2,0,1,6]
n=len(ar)
print(subarray(ar,n))
