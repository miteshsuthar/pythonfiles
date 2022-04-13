ar=[2,3,-3,4,-5,-6]
for i in range(len(ar)):
    sum =0
    for j in range(len(ar)):
        if abs(ar[i])==abs(ar[j] and i!=j):
            sum= abs(ar[i])*2
        else:
            sum =sum+ar[i]
    print(sum)
