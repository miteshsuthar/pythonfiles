def fib(n):
	a=0
	b=1
	for i in range(2,n+1):
		sum =a+b
		a=b
		b=sum
	return sum
result=fib(8)
print(result)																											