def insertion_sort(ar,n):     #the complexity of insertion sort is Order of n square= o(n**2)
    for pas in range(1,n):
        ele=ar[pas]
        j=pas-1
        while j>-1 and ar[j]>ele:
            ar[j+1]=ar[j]
            j-=1
        ar[j+1]=ele
ar=[20,15,17,14,12]
n=len(ar)
print(insertion_sort(ar,n))

