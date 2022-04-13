class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 
class Linkedlist:
    def __init__(self):
        self.start=None 
    
    def create(self):
        n=int(input("Enter the data"))
        ptr=Node(n)
        

    def traverse(self):
        ptr=self.start
        while ptr is not None:
            print(ptr.data)
            ptr=ptr.next
    def backword(self):
        
    
l=Linkedlist()
n=int(input("Enter the number how many element do you want to print"))
for i in range(n):
    l.create()
l.traverse()
l.backword()
