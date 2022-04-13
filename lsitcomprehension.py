from re import L
l2=[]
x=int(input())
y=int(input())
z=int(input())
n=3
l3=[]
l3.append(x)
l3.append(y)
l3.append(z)
for i in l3:
    for j in range(n):
       l2.append(l3[j])
       


# n=3
# l=[[j for j in range(n)] for j in range(n)]
# print(l)