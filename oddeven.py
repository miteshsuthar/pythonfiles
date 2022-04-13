def even():   
    ar1=[] 
    for i in range(1,n+1):
        if i%2==0:
            ar1.append(i)
    return ar1        
def odd():
    ar2=[]
    for j in range(1,n+1):
        if j%2!=0:
            ar2.append(j)
    return ar2
n=int(input())
ar3=[]
ar1=even()
ar2=odd()            
print(ar1+ar2)
