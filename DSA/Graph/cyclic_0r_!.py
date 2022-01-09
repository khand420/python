class Graph:
    def __init__(self,v ):
        # no of vertices graph 
        self.v = v 
        # adjacency List 
        self.adj = [0] * v 
        for i in range(self.v):
            self.adj[i] = []

    def addedge(self,i,j):
        self.adj[i].append(j)

    def isCycle(self):
        visited = [False] * self.v
        helper = [False] * self.v
        for i in range(self.v):
            if visited[i] == False:
                ans = self.DFS(i,visited,helper)
                if ans == True:
                    return True
        return False

    def DFS(self, i, visited, helper):
        visited[i] = True
        helper[i] = True
        neighbours = self.adj[i]
        for k in range(len(neighbours)):
            curr = neighbours[k]
            if helper[curr] == True:
                return True
            if visited[curr] == False:
                ans = self.DFS(curr,visited,helper)
                if ans == True:
                    return True
            helper[i] = False
            return False


if __name__ == "__main__":
    # No of nodes
    n = 4 
    g = Graph(n)  

    g.addedge(0, 1)
    # g.addedge(2, 2)                                
    # g.addedge(1, 3)     
    g.addedge(3, 1)           #add for make graph no cyclic                                                 
    g.addedge(1, 2)                                
    g.addedge(3, 0)                                

if g.isCycle() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")    
            
            # TechOUs/AlgoHeist
