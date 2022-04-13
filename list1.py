# n=int(input())
# m=int(input())
# matrix = [input().split() for i in range(n)]
# matrix= [[input() for j in range(m)] for i in range(n)] 

row=int(input("Enter number of rows you want: "))
col=int(input("Enter number of columns you want: "))
mat=[]
for m in range(row):
  a=[]
  for n in range(col):
     a.append(0)
  mat.append(a)

for i in range(len(mat)):
  for j in range(len(mat[0])):
    mat[i][j]=int(input("Input element: "))
print("Your Matrix is :",mat)