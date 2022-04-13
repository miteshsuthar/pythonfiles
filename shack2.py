#write a program to input value of two the square matrix 
row=int(input())
col=int(input())
matrix=[]
for m in range(row):
  a=[]
  for n in range(col):
      l=list(map(int,input().strip().split()))[:col]
      a.append(l)
  matrix.append(a)
print(matrix)