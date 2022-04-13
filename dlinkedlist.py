class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.start=None     
    def create(self):
        data=int(input('enter the data'))
        n=Node(data)
        if self.start is None:
            self.start=n
        else:
            ptr=self.start
            while ptr.next is not None:
                ptr=ptr.next
            ptr.next=n   
    def traverse(self):
        if self.start is None:
            print("Linkedlist is empty")
        else:
            ptr=self.start
            while ptr is not None:
                print(ptr.data)
                ptr=ptr.next

l=linkedlist()
n=int(input("Enter number of nodes"))
for i in range(n):
    l.create()
l.traverse()