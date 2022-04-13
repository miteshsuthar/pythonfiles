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
            self.start.prev=n
            self.start.next=n
        else:
            self.start.prev.next=n
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev=n 
        
    def deleteNode(self):
        pos=int(input("Enter the position which you want to delete the node "))
        num=self.countNode()  
        if pos<=0:
            pos=1
        if num+1<pos:
            print("position is Invalid ")
            pos=num+1
        if pos==1:
            ptr=self.start
            while ptr.next!=self.start:
                ptr=ptr.next
            ptr.next=self.start.next
            self.start=self.start.next 
            self.start.prev=ptr
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i+=1
            ptr.next=ptr.next.next  
            ptr.next.next.prev=ptr

    def traverse(self):
        if self.start is None:
            print("Linkedlist is empty")
        else:    
            ptr=self.start
            while ptr.next!=self.start:
                print(ptr.data)
                ptr=ptr.next
            print(ptr.data)
            
    
    def countNode(self):
        if self.start is None:
            return 0
        else:
            ptr=self.start
            count=1
            while ptr.next!=self.start:
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
            ptr=self.start
            while ptr.next!=self.start:
                ptr=ptr.next
            ptr.next=n
            n.next=self.start
            self.start.prev=n
            self.start=n
            n.prev=ptr
            # n.prev=self.start.prev
            # n.next=self.start
            # self.start.prev=n
        else:
            i=1
            ptr=self.start
            while i<pos-1:
                ptr=ptr.next
                i=i+1
            n.next=ptr.next
            ptr.next=n
            n.prev=ptr

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
            ptr=self.start.prev
        while ptr.prev!=self.start.prev:    
            print(ptr.data)
            ptr=ptr.prev
        print(ptr.data)

            # ptr=ptr.prev

                
        
          
l=Linkedlist()
n=int(input("Enter the number of data "))
for i in range(n):
    l.create()

l.traverse()
l.deleteNode()
# l.insert1()
l.traverse()
# print()
# l.backword()

