def comparision(st1,st2):
	if len(st1)!=len(st2):
		return False
	else:
		for i in range(0,4):
			if(st1[i]!=st2[i]):
				if(st1[i]=='x' or st2[i]=='x'):
					return True 
				return False
				
str1="sxse"
str2= "soxe"
result=comparision(str1,str2)
print(result)
