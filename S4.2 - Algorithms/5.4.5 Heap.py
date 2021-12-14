#Notes: Implementing a swap function is hard so swapping the values is an easier solution
#Notes: When deleting the root node, it is best to take the last element (The element which is furthest to the right of the tree and furthest to the bottom, if visualised that is) and put it at the root, afterwards you can just use the swap function to swap the values around so it matches the ascending or descending tree structure
#Notes: On having a root value higher than both children. Using the swap method along with an if condition on which of the 2 child notes is smaller, you can swap with the smallest one and therefore keep the ascending order intact

#Needs a parent?
class Heap:
  last_element = None
  root = None
  class HeapNode:  
    def __init__(self, data):
      self.left = None
      self.right = None
      self.parent = None
      self.data = data      

  #Insert method for creating nodes
  #Swap upward till the parent value isn't smaller than the current inserted value
  def InsertNode(self,insert_data):
    node = self.last_element    
    while node.parent != None:
      if node.parent.right == None or node.parent.right != node:
        break
      node = node.parent
    if node.parent != None and node.parent.right == None:
      node.parent.right = self.HeapNode(insert_data)
      node.parent.right.parent = node.parent
      self.last_element = node.parent.right
    else:
      while node.left != None:
        node = node.left
      node.left = self.HeapNode(insert_data)
      node.left.parent = node
      self.last_element = node.left
    self.Swap_Data(self.last_element)

  def Swap_Data(self):
    node = self.last_element
    while node.parent != None and node.data < node.parent.data:
      node.data, node.parent.data = node.parent.data, node.data
      node = node.parent
  
  #Method for printing the tree
  def PrintTree(self,list):
    if self.left:
      self.left.PrintTree(list)
    list.append(self.data),
    if self.right:
      self.right.PrintTree(list)

heap = Heap()
heap.InsertNode(10)
last_element = heap
heap.InsertNode(last_element,20)
heap.InsertNode(last_element,15)
heap.InsertNode(last_element,5)
heapList = []
heap.PrintTree(heapList)
print(heapList)
# Root = null, Bottom = null
# ()
#
# 1. Element => Root = newNode, Bottom = newNode
#   newNode.Parent = null;
#   
# 
# n'te element
#   a. Finde det sted den skal indsættes (som den nye bottom)
#   b. Indsætte den nye knude
#   c. Assign ny bottom
#
#        ()
#       /  \
#     ()   (.)
#    / \
#  ()  () 
#
# Finde ny bottom lokation:
# Gå op indtil der er en "ledig" vej til højre
# node = Bottom;
# while (node.Parent != null)
# {
#    if (node.Parent.Right == null || node.Parent.Right != node)
#    {
#       break;
#    }
#    node = node.Parent;
# }
# Nu er vi gået op indtil der er en leig vej til højre.
# if (node.Parent.Right == null)
# {
#     Node.Parent.Right = newNode;
#     newNode.Parent = node.Parent;
# }
# else
# {
#    Vi skal gå ned til venstre indtil vi ikke kan komme længere
#    while (node.Left != null)
#    {
#       node = noe.Left;
#    }
#
#    DEn nye knude skal indsættes som node.left
#    node.Left = newNode;
#    newNode.Parent = node;
# }
# Bottom = newNode
#
# Swap up indtil knuden er på plads
# node = Bottom
# while (Parent != null node.value < node.Parent.Value)
# {
  # node.value, node.parent.value = node.Parent.value, node.value;
#   node = node.parent
# }
