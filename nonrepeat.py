ar=[-1,2,-1,3,2]
print(ar)
for i in range(len(ar)):
    for j in range(len(ar)):
        if ar[i]==ar[j] and i!=j:
            j=len(ar)
            break
    if j==len(ar)-1:
        print(ar[i])


