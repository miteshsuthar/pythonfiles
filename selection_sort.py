ar=[20,15,17,14,10]
n=len(ar)
for i in range(1,n):
    min=i-1
    for j in range(i,n):
        if ar[j]<ar[min]:
            min=j
    ar[min],ar[i-1]=ar[i-1],ar[min]
print(ar)

# ar=[20,15,17,14,10]
# n=len(ar)
# minn=0
# for i in range(1,n):
#     ele=ar[i-1]
#     while  i<=n-1:
#         if ar[i]<ar[minn]:
#             minn=i
#             i+=1
#         else:
#             i+=1
#     ele,ar[minn]=ar[minn],ele
# print(ar)

