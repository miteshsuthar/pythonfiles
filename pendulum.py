def pendulum(ar,n):
    ar1=[]
    for i in range(n):
        if i==0:
            ar1.append(ar[i])
        else:
            if i%2!=0:
                ar1.append(ar[i])
            else:
                ar1.insert(0,ar[i])
    return ar1
# ar=[5,1,3,2,4]
ar=[1,8,9,7,5,6,11,18]         
# ar=[11,12,31,14,5]
ar.sort()
n=len(ar)
print(pendulum(ar,n))







    