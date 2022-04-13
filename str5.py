st='ABCDDDDDCCCBBBEE'
result=''
for i in range(0,len(st)):
		if st[i] not in result:
			result=result+st[i]		
print(result)
