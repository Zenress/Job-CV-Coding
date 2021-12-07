import random

class Node:
  #Initialising the class with a left and right variable
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  #Insert method for creating nodes
  def InsertNode(self,data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = Node(data)
        else:
          self.left.InsertNode(data)
      elif data > self.data:
        if self.right is None:
          self.right = Node(data)
        else:
          self.right.InsertNode(data)
    else:
      self.data = data
  
  #Find_value method to compare the value with other nodes
  def find_data(self,value):
    if value < self.data:
      if self.left is None:
        return str(value)+" Not found"
      return self.left.find_data(value)
    elif value > self.data:
      if self.right is None:
        return str(value)+" Not found"
      return self.right.find_data(value)
    else:
      print(str(self.data) + " is found")

  #Method for printing the tree
  def PrintTree(self,list):
    if self.left:
      self.left.PrintTree(list)
    list.append(self.data),
    if self.right:
      self.right.PrintTree(list)

root = Node(12)
root.InsertNode(6)
root.InsertNode(14)
root.InsertNode(3)
#Making a random 100 item list with numbers between 1 and 100
unsorted_data = [random.randrange(1,100,1) for i in range(100)]
for x in unsorted_data:
  root.InsertNode(x)

sorted_data = []
root.PrintTree(sorted_data)
print(sorted_data)