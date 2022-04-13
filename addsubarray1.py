ar=[14,20,14,30,14,75,24,14]
n=len(ar)
ar1=[]
ele=14
count=0
for i in range(n):
    if ele==ar[i]:
        count+=1
    else:
        ar1.append(ar[i])
for i in range(count):
    ar1.append(0)
print(ar1)


    
