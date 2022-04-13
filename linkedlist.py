from tracemalloc import start


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.start=None 
    def traverse(self):
        ptr=self.start
        while ptr is not None:
            print(ptr.data)
            ptr=ptr.next
        # print(n1.data,n2.data,n3.data)
        
n1=Node(100)
n2=Node(200)
n3=Node(300)
l=linkedlist()
l.start=n1
n1.next=n2
n2.next=n3
l.traverse()
