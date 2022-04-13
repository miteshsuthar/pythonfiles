def fun(n):
	print(n)
	# print("csd") 
	if n>0:
		fun(n-1)
	if n>1:
		fun(n-1) #fun(n-2) 
	print(n+n)
fun(3)
