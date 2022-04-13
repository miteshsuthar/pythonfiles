class Csd:
	x=10
	def __init__(self):
		self.y=20
c1=Csd();
c2=Csd();
p=c1.x
q=c1.y
r=c2.x
s=c2.y
c1.x=100
c2.y=1000
print(c1.x+c1.y+c2.x+c2.y+p+q+r+s)