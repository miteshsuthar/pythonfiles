# n = int(input())
# integer_list = map(int, input().split())
# t=tuple(integer_list)
t=(1,3,4,5)
sum=0
for i in t:
    sum=sum+i
print((hash(sum)))