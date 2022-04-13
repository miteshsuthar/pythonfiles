n=int(input("Enter the number "))
st=str(n)
l=len(st)
sum=0
for i in st:
    sum=sum+pow(int(i),l)

if sum==n:
    print("True")
else:
    print("False")

