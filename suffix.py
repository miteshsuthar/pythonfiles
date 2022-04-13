from audioop import reverse


n=3
# l1=['pqrstu', 'zxcstu' ,'prostu' ,'lmnstu' ,'zxystu']
l1=['chandr','chapl','chazp']
l2=[]
l=0
for i in range(n):
    for j in l1[i]:
        if j in l1[i+1]:
            l2.append(j)         
    break
l4=''.join(l2)
print(l4)
        
