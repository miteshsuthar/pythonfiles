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
        else:
            ptr=self.start
            while ptr.next is not None:
                ptr=ptr.next
            ptr.next=n
        
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
        else:
            ptr=self.start
            i=1
            while i<pos-1:
                ptr=ptr.next
                i+=1
            ptr.next=ptr.next.next    

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
    def reverse(self):
        ptr=self.start
        ptr1=ptr2=None
        while ptr!=None:
            ptr2=ptr.next 
            ptr.next=ptr1
            ptr1=ptr
            ptr=ptr2
        self.start=ptr1

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

    def midfind(self):
        if self.start is None:
            print("linkedlist is empty")
        ptr=ptr1=self.start
        while ptr!=None and ptr.next!=None :
            ptr=ptr.next.next
            if ptr!=None:
                ptr1=ptr1.next
        print(ptr1.data)

    def create_sorted(self):
        data=int(input("Enter data"))
        n=Node(data)
        if self.start is None:
            self.start=n
        else:
            if n.data<self.start.data:
                n.next=self.start
                self.start=n
            else:
                ptr=self.start
                ptr1=None
                while ptr!=None and ptr.data<n.data:
                    ptr1=ptr
                    ptr=ptr.next
                n.next=ptr1.next
                ptr1.next=n
    

l=Linkedlist()
n=int(input("Enter the number of data "))
for i in range(n):
    l.create_sorted()

# l.traverse()
# l.deleteNode()
# l.traverse()
# print()
# l.reverse()
l.traverse()
# print()
# l.midfind()


