# GRAPH
#### MAX IN OUT DEGREE
from collections import Counter 
class Graph:
  def __init__(self, dir = False):
    self.dir = dir
    self.graph = dict()
    
  def add_node(self, newnode):
    self.graph[newnode] = []

  def add_edge(self, st, ed): # st means startnode, ed means endnode
    if self.graph.get(st) is None:
      self.graph[st] = []
    if self.graph.get(ed) is None:
      self.graph[ed] = []

    self.graph[st].append(ed)
    if not self.dir:
      self.graph[ed].append(st)
  
  def remove_edge(self, st, ed): # st means starnode, ed means endnode
    self.graph[st].remove(ed)
    if not self.dir:
      self.graph[ed].remove(st)

  def printGraph(self):
      for x in self.graph:
        print(x, ":", self.graph[x])

  def printOutdegree(self):
    for x in self.graph:
        print("OutDegree of", x, ":", len(self.graph[x]))

  def printIndegree(self):
    merged_list = []
    for x in self.graph:
        merged_list += self.graph[x]
    indegree = Counter(merged_list)
    for x in indegree:
        print("Indegree of", x, ":", indegree[x])

  def findMaxInOutDegree(self):
    max_indegree = -1
    max_outdegree = -1 
    max_indegreeNodes=[]
    max_outdegreeNodes=[]


# finding nodes with maximum indegree
    merged_list = []
    for x in self.graph:
        merged_list += self.graph[x]
    indegree = Counter(merged_list)
    for x in indegree:
      if indegree[x] >= max_indegree:
        max_indegree = indegree[x]
    print(f'maximun indegree in this graph:{max_indegree}')
    for x in indegree:
      if max_indegree == indegree[x]:
        max_indegreeNodes.append(x)

# finding nodes with maximum outdegree
    for x in self.graph:
      if len(self.graph[x]) >= max_outdegree:
        max_outdegree = len(self.graph[x])
    print(f'maximun outdegree in this graph:{max_outdegree}')
    for x in self.graph:
      if max_outdegree == len(self.graph[x]):
        max_outdegreeNodes.append(x)

    return max_indegreeNodes, max_outdegreeNodes

# find_common_adjascent_node
  def find_common_adjascent_node(self, node1,node2):
    list1=[]
    list2=[]
    list1 = self.graph[node1]
    list2 = self.graph[node2]
    mutualFriend =[]
    
    count=0
    for x in list1:
      if x in list2:
        mutualFriend.append(x)
        count+=1
    if count==0:
      print("No adjascent nodes between them")
    else:
       print("Common adjascent node between", node1 ,"and", node2, ":")
       print(mutualFriend)

#sink nodes = nodes with zero outdegree
  def printSinkNodes(self):
    sink_nodes = []
    for x in self.graph:
      if len(self.graph[x])==0:
        sink_nodes.append(x)
    print(sink_nodes)

gr = Graph(True)
gr.add_node(0)
gr.add_node(1)
gr.add_node(2)
gr.add_node(3)
gr.add_node(4)

gr.add_edge(0,1)
gr.add_edge(0,2)
gr.add_edge(1,0)
gr.add_edge(2,3)
gr.add_edge(3,0)
gr.add_edge(3,4)
gr.add_edge(4,4)

gr.printGraph()
gr.printIndegree()
gr.printOutdegree()

print(gr.findMaxInOutDegree())

#find_common_adjascent_node
gr = Graph(True) #Directed graph
gr.add_node('A')
gr.add_node('B')
gr.add_node('C')
gr.add_node('D')
gr.add_node('E')
gr.add_node('F')
gr.add_node('G')
gr.add_node('H')
gr.add_edge('A','B')
gr.add_edge('A','G')
gr.add_edge('A','D')
gr.add_edge('B','A')
gr.add_edge('B','F')
gr.add_edge('B','E')
gr.add_edge('C','F')
gr.add_edge('C','H')
gr.add_edge('D','F')
gr.add_edge('D','A')
gr.add_edge('E','B')
gr.add_edge('E','G')
gr.add_edge('F','B')
gr.add_edge('F','D')
gr.add_edge('F','C')
gr.add_edge('G','A')
gr.add_edge('G','E')
gr.add_edge('H','C')
gr.printGraph()


gr.find_common_adjascent_node( 'A', 'C')
gr.find_common_adjascent_node( 'A', 'F')
gr.printSinkNodes()
