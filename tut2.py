#method 
class Student:
	cname="class"
	def __init__(self,first,second):
		self.first=first 
		self.second= second
s=Student(12,13)
s1=Student(14,16)
print(s.first,s.second,s.cname)
print(s1.first,s1.second,s.cname)
Student.cname="Method"
s1.third =15
del s.first 
print(s1.first,s.second,s.cname,s1.third)
print(s.__dict__)
print(s1.__dict__)


