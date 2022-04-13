def sumn(n):
	if n==0:
		return 0
	else:
		return sumn(n-1)+n
result=sumn()
print(result)