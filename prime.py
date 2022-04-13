
def primenumber(ar):
    ar1=[]
    ar2=[]
    for i in ar:
        if  i==2:
            ar1.append(i)
        if i==1:
            ar2.append(i)
        for j in range(2,i):
            if i%j==0 and i!=j:
                ar2.append(i)
                break
            else:
                ar1.append(i)
                break
    return ar1+ar2
# ar=[1,8,2,3,4,5,7,20]
ar=[2,3,4,5,6,7,8,9,10]

print(primenumber(ar))


    