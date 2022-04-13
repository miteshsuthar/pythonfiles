
# for i in range(n-1):
#     count=0
#     for j in ar[i]:
#         print(j)
#         if j==ar[s][k]:
#             count+=1
#             print(count)
#             k+=1
#         break
#     s+=1
#     if count<minimum:
#         print(count)
#         minimum=count
# # minimum=3
# print(minimum)
# print(ar[0][:minimum])
# m=len(ar[0])
# i = 0
# reference = ar[0]
# while i < m:        
#     for myStr in ar:
#         if myStr[i] != reference[i]:
#             print(reference[:i])
#             break
#     i += 1
 
# from ast import Str


def longestCommonPrefix(self, strs):
    if not strs:
        return ''
    for i in range(len(strs[0])):
        char = strs[0][i]
        for j in range(1,len(strs)):
            if i == len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
        

Strs=['chandrapal','chandler','characteristics','channelization']
# Strs=['hello','world']
n=len(Strs)
print(longestCommonPrefix(n,Strs))
