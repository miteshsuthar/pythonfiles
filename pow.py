def pow(a,b):
	if b==0 :
		return 1
	else:
	   return pow(a,b-1)*a

result=pow(3,3)
print(result)

