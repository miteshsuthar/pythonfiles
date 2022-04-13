r,c= map(int, input().split())
matrix=[]
matrix1=[]
sum=[]
for i in range(r): 
    ar1=[]
    row = list(map(int, input().split()))
    matrix.append(row)
for i in range(c):
    for j in range(r):
        print(matrix[j][i],end=' ')    
    print()