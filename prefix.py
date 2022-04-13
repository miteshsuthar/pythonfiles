l2=['chandrapal','chanactor','chandler','chanrdf']
n=4
l1=[]
for i in range(n):
    for j in l1[i]:
        if j in l1[i]:
            l2.append(j)         
    break
l4=''.join(l2)
print(l4)
        