n=(input())
ar2=[];
ar1=[] 
for i in range(1,n+1):
    if(i%2==0):
        {ar1.append(i)}
    else:
        {ar2.append(i)}            
print(ar1+ar2)
