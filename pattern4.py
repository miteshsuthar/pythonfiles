# 1
# * *
# 2 3 4
# * * * *
# 5 6 7 8 9
# n=int(input())
# count=1
# for i in range(n):
#     for j in range(i+1):
#         if i%2!=0:
#             print("*",end=' ')
#         else:
#             print(count,end=' ')
#             count+=1            
#     print()

# 1
# 2 6  
# 3 7 10
# 4 8 11 13
# 5 9 12 14 15

n=int(input())
for i in range(n):
    flag=4
    count=i
    for j in range(i+1):
        if count==1:
            print(count)
        else:
            print(count+flag,end=' ')
            count+=1       
            flag-=1     
    print()