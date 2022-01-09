# BFS Graph Traversal steps:

# 1.Enqueue the First vertex.
# 2.Loop --- while(Queue Not Empty):
#          i. curr = dequeue()& print. Check its adjacent vertex (Not visited one)
#          ii. Enqueue all its adjancent vertex.

# 3. If all adjacent vertex are visited.Ingnore

# QUEUE-> follows FIFO 


queue = [] #initialize a queue
visited =[]

def bfs(graph, node):
    queue.append(node)
    visited.append(node)
    while queue:
        curr = queue.pop(0)
        print (curr, end= " ")

        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

# bfs(graph, node='A')




# DFS Graph Traversal steps

# 1.Push & print First vertex into stack
# 2.Loop --- while(stack Not empty):
#            curr = top()
#            Check and push & print only one adjacent vertex
#                         (Not visited One)
# 3. If all adjacent vertex are visited.pop     

# STACK-> follows LIFO 



# queue = []
visited =[]     #Set to keep track of visited nodes in STACK

def dfs(graph, node):
   if node not in visited:
       print(node)
       visited.append(node)
       for neighbour in graph[node]:
           dfs(graph, neighbour)
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

dfs(graph, node='A')



# --------------BFS                    DFS-----------------

        #    1. Level                  1. Depth
        #    2. Queue                  2. Stack
        #    3. FIFO                   3. LIFO
        #    4. All adjacent           4. One adjacent 
        #     vertex en-queue here      vertex add in stack at a time
        #    5.more memory             5.less memory as compare to BFS