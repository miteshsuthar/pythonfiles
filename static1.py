class Student:
	cname="codeplanet"
	def __init__(self,rollno,name,z):
		self.rollno=rollno
		self.name=name 
		self.x=z
s1=Student(1,"abc",100)
s2=Student(2,"xyz",200)
Student.y=100
print(s1.rollno,s1.cname)
s1.rollno=100
s1.name="cpt"
Student.cname ="cdpd"
print(s1.rollno,s1.name,s1.y,s1.x)
print(s2.rollno,s2.name,Student.x)