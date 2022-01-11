import sys

class Graph:
  nodes = []

  def InsertNode(self,node):
    self.nodes.append(node)

  priorityQueue = []
  #Add to a queue/list and then just print out the list?
  def Dijkstra(self,startNode):
    for x in self.nodes:
      x.weight = sys.maxsize
    startNode.weight = 0
    self.priorityQueue.append(startNode)
    while len(self.priorityQueue) > 0:
      node = self.popSmallest()
      neighbours = node.Visit()
      for x in neighbours:
        if x.endNode != node:
          self.priorityQueue.append(x.endNode)
        else:
          self.priorityQueue.append(x.startNode)

  def popSmallest(self):
    smallestNr = sys.maxsize
    for x in self.priorityQueue:
      if x.weight < smallestNr:
        smallestNr = x.weight
        candidate = x
    self.priorityQueue.remove(candidate)
    return candidate

  class node:
    def __init__(self, name, visited = False,):
      #Instead of a value
      self.name = name  
      self.visited = visited
      self.edges = []
      self.weight = 0
      self.parent = None
    
    def AddEdge(self,edge):
      self.edges.append(edge)

    def Visit(self):
      if self.visited is not True:
        self.visited = True
        self.printPath()
        print(self.weight)
        print()
        for x in self.edges:
          if x.endNode != self:
            x.endNode.SOLVisit(self.weight + x.weight,self)
          else:
            x.startNode.SOLVisit(self.weight + x.weight,self)
        return self.edges
      else:
        return []

    def SOLVisit(self, weight,parent):
      if weight < self.weight:
        self.weight = weight
        self.parent = parent

    def printPath(self):
      if self.parent is not None:
        self.parent.printPath()
      print(self.name)  

  class edge:
    def __init__(self, startNode, endNode, weight):
      self.startNode = startNode
      self.endNode = endNode
      self.weight = weight

myGraph = Graph()
nodeA = myGraph.node("A")
nodeB = myGraph.node("B")
nodeC = myGraph.node("C")
nodeD = myGraph.node("D")
nodeE = myGraph.node("E")
nodeF = myGraph.node("F")
nodeG = myGraph.node("G")
nodeH = myGraph.node("H")

edgeAB = myGraph.edge(nodeA,nodeB,10)
nodeA.AddEdge(edgeAB)
nodeB.AddEdge(edgeAB)

edgeAE = myGraph.edge(nodeA,nodeE,18)
nodeA.AddEdge(edgeAE)
nodeE.AddEdge(edgeAE)

edgeAC = myGraph.edge(nodeA,nodeC,10)
nodeA.AddEdge(edgeAC)
nodeC.AddEdge(edgeAC)

edgeAD = myGraph.edge(nodeA,nodeD,15)
nodeA.AddEdge(edgeAD)
nodeD.AddEdge(edgeAD)

edgeBG = myGraph.edge(nodeB,nodeG,15)
nodeB.AddEdge(edgeBG)
nodeG.AddEdge(edgeBG)

edgeBE = myGraph.edge(nodeB,nodeE,13)
nodeB.AddEdge(edgeBE)
nodeE.AddEdge(edgeBE)

edgeEH = myGraph.edge(nodeE,nodeH,13)
nodeE.AddEdge(edgeEH)
nodeH.AddEdge(edgeEH)

edgeEF = myGraph.edge(nodeE,nodeF,20)
nodeE.AddEdge(edgeEF)
nodeF.AddEdge(edgeEF)

edgeEC = myGraph.edge(nodeE,nodeC,15)
nodeE.AddEdge(edgeEC)
nodeC.AddEdge(edgeEC)

edgeEG = myGraph.edge(nodeE,nodeG,15)
nodeE.AddEdge(edgeEG)
nodeG.AddEdge(edgeEG)

edgeCD = myGraph.edge(nodeC,nodeD,9)
nodeC.AddEdge(edgeCD)
nodeD.AddEdge(edgeCD)

edgeFD = myGraph.edge(nodeF,nodeD,8)
nodeF.AddEdge(edgeFD)
nodeD.AddEdge(edgeFD)

edgeFH = myGraph.edge(nodeF,nodeH,10)
nodeF.AddEdge(edgeFH)
nodeH.AddEdge(edgeFH)

edgeHG = myGraph.edge(nodeH,nodeG,20)
nodeH.AddEdge(edgeHG)
nodeG.AddEdge(edgeHG)

myGraph.InsertNode(nodeA)
myGraph.InsertNode(nodeB)
myGraph.InsertNode(nodeC)
myGraph.InsertNode(nodeD)
myGraph.InsertNode(nodeE)
myGraph.InsertNode(nodeF)
myGraph.InsertNode(nodeG)
myGraph.InsertNode(nodeH)

myGraph.Dijkstra(nodeG)