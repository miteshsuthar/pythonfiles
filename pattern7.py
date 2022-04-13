n = int(input("Enter the number of rows: "))  
m = (2 * n) - 2  
for i in range(0, n):  
    count=1
    for j in range(0, m):  
        print(end=" ")  
    m = m - 1  # decrementing m after each loop  
    for j in range(0, i + 1):  
        # printing full Triangle pyramid using stars  
        print(count, end=' ')
        count+=1  
    print(" ")  