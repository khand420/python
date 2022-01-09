# Adjacency Matrix -> Undirected Graph
# Adjacency List -> we use Linked list Directed Graph or Undirecte graph both




#                       Adjacency-Matrix         Adjacency-List  

# Time Complexity ->         O(1)                 O(V+E)
# Space Complexity  ->       O(n^2)                O(V+E)




# Adjacency-List example
adj_list ={"A":["B", "C"],
           "B":["A","D","E"],
           "C":["A","D"],
           "D":["C","B","E"],
           "E":["B","D"]
}
# print(adj_list["B"])

print(adj_list["A"].append("D"))
print(adj_list["D"].append("A"))
# print(adj_list)




# 1. DIRECTED LINKED LIST  GRAPH
edges =[("A","B"),("A","C"),("B","C"),("B", "D"),
        ("B", "E"),("C","D"),("D","E")]

class Graph:
    def __init__(self,Nodes):
        self.nodes= Nodes
        self.adj_list={}
        
        for node in self.nodes:
            self.adj_list[node]=[]

    def add_edge(self,v,e):
        self.adj_list[v].append(e) 
        self.adj_list[e].append(v)

    def degree_vertex(self, node):
        degree =len(self.adj_list[node])
        return degree   

    def print_adj(self):
        for node in self.nodes:
            print(node,":",self.adj_list[node])


nodes = ["A", "B", "C", "D", "E"]
graph = Graph(nodes)
for v,e in edges:
    graph.add_edge(v,e)

graph.print_adj()  #print all the adjency vertices

print("Degree of vertices",graph.degree_vertex("B"))  #for find degree of vertex




# 2.UN-DIRECTED LINKED LIST GRAPH
edges =[("A","B"),("A","C"),("B","C"),("B", "D"),
        ("B", "E"),("C","D"),("D","E")]

class Graph:
    def __init__(self,Nodes, is_directed=False):
        self.nodes= Nodes
        self.adj_list={}
        self.is_directed =is_directed
        
        for node in self.nodes:
            self.adj_list[node]=[]

    def add_edge(self,v,e):
        self.adj_list[v].append(e) 
        # self.adj_list[e].append(v)
        if not self.is_directed:
            self.adj_list[e].append(v)

    def degree_vertex(self, node):
        degree =len(self.adj_list[node])
        return degree   

    def print_adj(self):
        for node in self.nodes:
            print(node,":",self.adj_list[node])



nodes = ["A", "B", "C", "D", "E"]
graph = Graph(nodes, is_directed=True) #change only
for v,e in edges:
    graph.add_edge(v,e)

graph.print_adj()  #print all the adjency vertices

print("Degree of vertices",graph.degree_vertex("B"))  #for find degree of vertex