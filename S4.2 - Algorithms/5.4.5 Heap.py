#Notes: Implementing a swap function is hard so swapping the values is an easier solution
#Notes: When deleting the root node, it is best to take the last element (The element which is furthest to the right of the tree and furthest to the bottom, if visualised that is) and put it at the root, afterwards you can just use the swap function to swap the values around so it matches the ascending or descending tree structure
#Notes: On having a root value higher than both children. Using the swap method along with an if condition on which of the 2 child notes is smaller, you can swap with the smallest one and therefore keep the ascending order intact

class HeapNode:
  def __init__(self, data):
    self.left = None
    self.right = None
    self.data = data

  #Insert method for creating nodes
  def InsertNode(self,data):
    if self.data:
      if data < self.data:
        if self.left is None:
          self.left = HeapNode(data)
        else:
          self.left.InsertNode(data)
      elif data > self.data:
        if self.right is None:
          self.right = HeapNode(data)
        else:
          self.right.InsertNode(data)
    else:
      self.data = data