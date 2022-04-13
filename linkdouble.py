from turtle import backward


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None  

class Linkedlist:
    def __init__(self):
        self.start=None 
    def create(self):
        data=int(input("Enter data"))
        n=Node(data)
        if self.start is None:
            self.start=n
        else:
            ptr=self.start
            while ptr.next is not None:
                ptr=ptr.next
            ptr.next=n
            n.prev=ptr  
        
    def deleteNode(self):
        pos=int(input("Enter the position which you want to delete the node "))
        num=self.countNode()  
        if pos<=0:
            pos=1
        if num+1<pos:
            print("position is Invalid ")
            pos=num+1
        if pos==1:
           self.start=self.start.next 
           self.start.prev=None
        else:
            ptr=self.start
            i=1
            while i<pos:
                ptr=ptr.next
                i+=1
            ptr.prev.next=ptr.next
            ptr.next.prev=ptr.prev  

    def traverse(self):
        ptr=self.start
        while ptr is not None:
            print(ptr.data)
            ptr=ptr.next
    
    def countNode(self):
        if self.start is None:
            return 0
        else:
            ptr=self.start
            count=1
            while ptr.next is not None:
                ptr=ptr.next
                count+=1
            return count 


    def insert1(self):
        pos=int(input("Enter the position of node"))
        num=self.countNode()  
        if pos<=0:
            pos=1
        if num+1<pos:
            
            print("position is Invalid ")
            pos=num+1

        data=int(input("Enter the data "))
        n=Node(data)
        if pos==1:
            n.next=self.start
            self.start=n
        else:
            i=1
            ptr=self.start
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            n.next=ptr.next
            ptr.next=n

    def insert(self):
        pos=int(input("Enter the position of node"))
        data=int(input("Enter the data "))
        n=Node(data)
        if pos==1:
            n.next=self.start
            self.start=n
        else:
            i=1
            ptr=self.start
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            n.next=ptr.next
            ptr.next=n
        
    def backword(self):
        if self.start is None:
           print ("the linkedlist is empty")
        else:
            ptr=self.start
        while ptr.next is not None:
            ptr=ptr.next
        while ptr is not None:    
            print(ptr.data)
            ptr=ptr.prev

            # ptr=ptr.prev
    def reverse(self):
        ptr=self.start
        while ptr is not None:
            ptr1=ptr.prev
            ptr.prev=ptr.next
            ptr.next=ptr1
            ptr=ptr.prev
        self.start=ptr 
l=Linkedlist()
n=int(input("Enter the number of data "))
for i in range(n):
    l.create()
# l.backword()
l.traverse()
# l.deleteNode()
l.reverse()
l.traverse()

