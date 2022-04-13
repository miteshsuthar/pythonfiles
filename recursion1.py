def fun(n):
	print(n)
	if n<10:
		print("Hello")
		fun(n*2)
		print(n)
	print(n+n)
fun(3)
