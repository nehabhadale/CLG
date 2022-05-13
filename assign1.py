'''
  0--- 1   
  \   / 
    2 --- 3
start with 2 node 
BFS ->
2 0 3 1
DFS ->
2 0 1 3
'''

from collections import defaultdict
 
global V
class Graph:
 
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    # Print the graph
    def print_graph(self):
        for i in range(V):
            print("Vertex " + str(i) + ":", end="")
            for j in self.graph[i]:
                print(" -> {}".format(j), end=" ")
                
            print(" \n")

    def DFS_rec(self,src,visited):
        visited[src]=True
        print(src , end=" ")
        for i in self.graph[src]:
            if visited[i]==False:
                self.DFS_rec(i,visited)

            
    # DFS 
    def DFS(self,src):
        visited = [False] * V
        self.DFS_rec(src,visited)

    
    
    #BFS
    def BFS(self,src):
      
        visited = [False] *V
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(src)
        visited[src] = True
 
        while queue:
 
            s = queue.pop(0)
            print (s, end = " ")
 
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 




V= int(input("Enter total number of vertex :"))
g=Graph()
e=int(input("\nEnter no. of edges :"))

for i in range(e):
    s=int(input("\nSource vertex :"))
    d=int(input("Destination vertex :"))
    g.addEdge(s, d)

g.print_graph()
while True:
    print("\n1.BFS \n2.DFS")
    ch=int(input("Enter choice :"))
    if ch==1:
        n=int(input("Enter start node :"))
        print("\nBFS -> ")
        g.BFS(n)
    elif ch==2:
        n=int(input("Enter start node :"))
        print("\nDFS -> ")
        g.DFS(n)
    else :
        break

'''
2 -> 0,
0 -> 2, 
1 -> 2, 
0 -> 1, 
2 -> 3,
1 -> 3 



BFS
Enter start node :2
2 0 3 1 

DFS
Enter start node :2
2 0 1 3 

'''