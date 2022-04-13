s=input()
num=0
for i in s:
    num=num+ord(i)
sum = 0
temp = num
k=0
# num=371Van
while num!=0:
    
    num//=10
    k+=1
print(num)

while temp > 0:
   digit = temp % 10
   sum += digit ** k
   temp //= 10
l=[]
# display the result
if num == sum:
    for i in s:
        if i not in l:
            l.append(i)
    print(''.join(l))
else:
   print(-1)