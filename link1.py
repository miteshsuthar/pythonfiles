from msilib import datasizemask
from re import L
from tracemalloc import start


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None 

class Linkedlist:
    def __init__(self):
        self.start=None 
    def traverse(self):
        ptr=self.start
        while ptr is not None:
            print(ptr.data)
            ptr=ptr.next
        

n=Node(100)
n1=Node(200)
n2=Node(300)
n3=Node(400)
l=Linkedlist()
l.start=n
n.next=n1
n1.next=n2
n2.next=n3
l.traverse()
