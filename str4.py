##output = cpoldaenet
#def merge(st1, st2):
#	i=j=0
#	result=""
#   while i<len(st1) and j<len(st2):
#	   result+=st1[i]+st2[j]
#	   i+=1
#	   j+=1
#	   while i<len(st1):
#		   result+=st1[i]
#		   i+=1
#	   while j < len(st2):
#		result += st2[j]
#		j += 1
#   return result
#'
#print(merge(st1,st2))

def solve(s, t):
   i = j = 0
   result = ""
   while i < len(s) and j < len(t):
      result += s[i] + t[j]
      i+=1
      j+=1
   while i < len(s):
      result += s[i]
      i += 1
   while j < len(t):
      result += t[j]
      j += 1
   return result
s='code'
t='planet'
print(solve(s, t))