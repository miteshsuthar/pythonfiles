def fun(n):
	#print(n) #tail recursion 
	if n>0:
		fun(n-1)
	#print(n) #Head recursion 
fun(3)
	  