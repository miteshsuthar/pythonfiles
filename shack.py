# li=[i for i in range(1,101)]
# sum=0
# for i in li:
#     sum=sum+int(i)
# print(sum)
# n=int(input())
# li=[i for i in range(1,n+1)]
# print(li)
s2=5050
n=100
# for i in range(1,n+1):
s1= list(map(int,input().strip().split()))[:n]
for i in s1:
    sum=sum+int(i)
print(sum)
print(s2-s1)