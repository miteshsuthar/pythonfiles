st=input()
print('Element ','|','symbol    ','|','Adress')
for i in range(len(st)):
	if st[i].isalpha():
		print(st[i],'      ','|','identifier','|',id(st[i]))
	else:
		print(st[i],'      ','|','Operator  ','|',id(st[i]))