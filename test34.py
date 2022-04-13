r,c= map(int, input().split())
matrix=[]
for i in range(r): 
    ar1=[]
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)
for i in range(r):
    sum=0
    for j in range(c):
        sum=sum+matrix[i][j]
    print(sum)