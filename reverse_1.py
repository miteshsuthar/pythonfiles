#left shift 
ar=[2,4,6,3,5,7,9]
print(ar)
def swap(i,j):
	temp=ar[i]
	ar[i]=ar[j]
	ar[j]=temp
i=0
j=i+1
l=len(ar)
while i<j:
	swap(i,j)
	i=i+1
	j=j+1
	if l==j:
		break
	
print(ar)