class Graph:
  nodes = []

  def InsertNode(self,node):
    self.nodes.append(node)

  queue = []
  #Add to a queue/list and then just print out the list?
  def BreadthWriteGraph(self,startNode):
    self.queue.append(startNode)
    while len(self.queue) > 0:
      node = self.queue.pop(0)
      neighbours = node.Visit()
      for x in neighbours:
        if x.endNode != node:
          self.queue.append(x.endNode)
        else:
          self.queue.append(x.startNode)

  class node:
    def __init__(self, name, visited = False):
      #Instead of a value
      self.name = name  
      self.visited = visited
      self.edges = []
    
    def AddEdge(self,edge):
      self.edges.append(edge)

    def DepthWriteGraph(self):  
      if self.visited is not True:
        self.visited = True
        print(str(self.name))
        for x in self.edges:
          if x.endNode != self:
            x.endNode.DepthWriteGraph()
          else:
            x.startNode.DepthWriteGraph()

    def Visit(self):
      if self.visited is not True:
        self.visited = True
        print(str(self.name))
        return self.edges
      else:
        return []

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

myGraph.BreadthWriteGraph(nodeA)
print()
#nodeA.DepthWriteGraph()