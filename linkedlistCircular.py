class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class Linkedlist:
    def __init__(self):
        self.start=None 
    def create(self):
        data=int(input("Enter data"))
        n=Node(data)
        if self.start is None:
            self.start=n
            self.start.next=self.start
        else:
            ptr=self.start
            while ptr.next!=self.start:
                ptr=ptr.next
            ptr.next=n
            n.next=self.start
        
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
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i+=1
            ptr.next=ptr.next.next    

    def traverse(self):
        if self.start is None:
            print("Linkedlist is empty")
        else:
            print(self.start.data)   
            ptr=self.start.next
            while ptr!=self.start:
                print(ptr.data)
                ptr=ptr.next
    
    def countNode(self):
        if self.start is None:
            return 0
        else:
            ptr=self.start
            count=1
            while ptr.next !=self.start:
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
        
          
l=Linkedlist()
n=int(input("Enter the number of data "))
for i in range(n):
    l.create()
l.traverse()
l.deleteNode()
# l.insert1()
l.traverse()

