# # 5
# # 2 1 3 28 9
ar=[4,91,5,3]
# temp=[]
n=4
count=0 
for i in range(n):
    for j in range(n):
        if i!=j and j<n-1:
            sal1=ar[i]**3+ar[j]**3
            if sal1 in ar:
                count+=1
            break
print(count)
# ar=[4,91,5,3]
# n=4
# i=0
# j=1
# count=0
# while(j<n-1):
#         sal1=ar[i]**3+ar[j]**3
#         i+=1
#         j+=1
#         if sal1 in ar:
#             count+=1
# print(count)


