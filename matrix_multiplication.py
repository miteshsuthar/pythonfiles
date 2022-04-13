print("Enter the first matrix row and column: ")
r, c = map(int, input().split())
print("Enter the second number of matrix row and column: ")
r1, c1 = map(int, input().split())
if c!=r1:
    print("It is not right matrices and not applicable to multiplcation ")

else:
    matrix=[]
    matrix1=[]
    for i in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(matrix)
    for i in range(c1):
        column = list(map(int, input().split()))
        matrix1.append(column)
    print(matrix1)
    # for i in range(c):
    #     sum=0
    #     for j in range(r):
    #         sum=sum+matrix[j][i]
    #     print(sum)
    