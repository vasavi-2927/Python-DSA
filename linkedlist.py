class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Linkedlist:
  def __init__(self):
    self.head=None
  def add(self,data):
    obj=Node(data)
    if self.head==None:
      self.head=obj
      return

    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=obj
  def traverse(self):
    cn=self.head
    while cn.next is not None:
      print(cn.data,end="->")
      cn=cn.next
    print(cn.data)
  def delfirst(self):
    self.head=self.head.next
  def dellast(self):
    self.head.next.next=None
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.traverse()
ll.delfirst()
ll.traverse()
ll.dellast()
ll.traverse()