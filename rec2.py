def fun(n):
	if n<10:
	   return fun(n*2)+n
	else:
		return 1

result =fun(3)
print(result)
