class Student:
	cname=("codeplanet") 
	def __init__(self,rollno, names):
			self.rollno=rollno
			self.names=names

s1 = Student (1,"abc")
s2 = Student (2,"par")
print(s1.rollno, s1.names, s1.cname) 
print(s2.rollno, s2.names,s1.cname)
s1.rollno = 100 
Student.cname ="Git"
print(s1.rollno,s1.names,s1.cname)
print(s2.rollno,s2.names,s2.cname)