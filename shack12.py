def rev(start,end,arr):
	i=start 
	j=end-1 
	while i<j:             
		temp=arr[i]          
		arr[i]=arr[j]                 
		arr[j]=temp
		i=i+1  
		j=j-1                                    
def rev_K(arr,n,k):
	for i in range(0,n,k):          
		start=i 
		end=k+i  
		if end<n:
			rev(start,end,arr)
		else:
			end=n 
			rev(start,end,arr)
			break
arr=[1,2,3,4,5]
k=3
n=len(arr)
rev_K(arr,n,k)
print(arr)