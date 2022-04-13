r, c = map(int, input().split())
matrix1=[]
matrix2=[]
for i in range(r):
    row = list(map(int, input().split()))
    matrix1.append(row)
for i in range(r):
    row = list(map(int, input().split()))
    matrix2.append(row)
for i in range(r):
    sum=0
    for j in range(c):
        sum=matrix1[i][j]+matrix2[i][j]
        print(sum,end=' ')
    print()
    