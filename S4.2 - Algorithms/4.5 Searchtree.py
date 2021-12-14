class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#Function for inserting values into the right places
def Insert(node,key):
    #If the starting node doesn't exist, create one
    if node is None:
        return Node(key)
    else:
        if node.val == key:
            return node
        #If the current parent value is lower than the insert value, go to the right and insert node there
        elif node.val < key:
            node.right = Insert(node.right,key)
        #If the current parent value is higher than the insert value, go to the right and insert node there
        else:
            node.left = Insert(node.left, key)
    #If there is only 1 node, it will return that node
    return node

#Function for traversing the tree in order of ascending numbers
def Inorder(node):
    if node:
        Inorder(node.left)
        print(node.val)
        Inorder(node.right)

def WriteTree(node):
    WriteTree_Rec(node, "")

def WriteTree_Rec(node, indent):
    if node is not None:
        print(indent + str(node.val))
        WriteTree_Rec(node.left, indent+"  ")
        WriteTree_Rec(node.right, indent+"  ")
    else:
        print(indent+"X")

def Search(node,key):
    #If node is null or key is present at node just return the node
    if node is None or node.val == key:
        return node
    #If the key value is higher than the node value, go to the right
    if node.val < key:
        return Search(node.right,key)
    #Else go to the left
    return Search(node.left,key)

#Inserting the parent node (A node without parents is a parent node in itself)
bst = Node(50)
bst = Insert(bst, 30)
bst = Insert(bst, 20)
bst = Insert(bst, 40)
bst = Insert(bst, 70)
bst = Insert(bst, 60)
bst = Insert(bst, 80)

Inorder(bst)
print(Search(bst, 30).val)
WriteTree(bst)