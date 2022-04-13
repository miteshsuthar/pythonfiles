from tracemalloc import start
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None 
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
            n.prev=ptr  
    def CountNodes(self):
        if self.start is None:
            return 0
        else:
            ptr=self.start
            count=1
            while ptr.next is not None:
                ptr=ptr.next
                count=count+1
            return count
    def insert(self):
        pos=int(input('enter the position'))
        n=self.CountNodes()
        if pos<=0:
            pos=1
        if pos>n+1:
            pos=n+1
        data=int(input("Enter the data"))
        n=Node(data)
        if pos==1:
            n.next=self.start
            self.start.prev=n
            self.start=n
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            n.next=ptr.next
            ptr.next=n
            n.prev=ptr
            n.next=ptr.next
            n.next.prev=n
            ptr.next=n    
    def insert1(self):
        pos=int(input('enter the position'))
        n=self.CountNodes()
        while pos<=0 or pos>n:
            print("Enter valid position")
            pos=int(input('enter the position'))
        data=int(input('enter the data'))
        n=Node(data)
        if pos==1:
            n.next=self.start
            self.start=n
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            n.prev=ptr
            n.next=ptr.next
            n.next.prev=n
            ptr.next=n     
    def delete(self):
        pos=int(input("Enter position of node which you want to delete"))
        n=self.CountNodes()
        while pos<=0 or pos>n:
            print("Enter valid position")
            pos=int(input('enter the position'))
        if pos==1:
            self.start=self.start.next
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            ptr.next=ptr.next.next
    def traverse(self):
        if self.start is None:
            print("Linkedlist is empty")
        else:
            ptr=self.start
            while ptr is not None:
                print(ptr.data)
                ptr=ptr.next
        # print(n1.data,n2.data,n3.data)
    def exchange(self):
        pos=int(input('enter the position'))
        n=self.CountNodes()
        while pos<=0 or pos>n:
            print("Enter valid position")
            pos=int(input('enter the position'))
        if pos==1:
            self.start=n
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            ptr.data=int(input("enter the data"))
            # ptr.next=n    
                

    def backword(self):
        if self.start is None:
            print("Linkedlist is empty")
        else:
            ptr=self.start
            while ptr.next is not None:
                ptr=ptr.next
            while ptr is not None:
                print(ptr.data)
                ptr=ptr.prev
    def DeleteNode(self):
        pos=int(input("Enter the position")) 
        if pos==1:
            self.start=self.start.next
        else:
            ptr=self.start
            i=1
            while i<pos:
                ptr=ptr.next
                i=i+1
            ptr.prev.next=ptr.next
            ptr.next.prev=ptr.prev


l=linkedlist()
n=int(input("Enter number of nodes"))
for i in range(n):
    l.create()
l.traverse()
l.insert()
l.traverse()