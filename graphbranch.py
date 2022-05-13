def addEdge(adj, v, w):
     
    adj[v].append(w)     
    adj[w].append(v) 
    return adj

 

def greedyColoring(adj, V, n):
     
    result = [-1] * V   
    result[0] = 0
 

    available = [False] * V
 
    # Assign colors to remaining V-1 vertices
    for u in range(1, V):           
         
        for i in adj[u]:      # Process all adjacent vertices and flag their colors as unavailable
            if (result[i] != -1):
                available[result[i]] = True           

    
        cr = 0       # Find the first available color
        while cr < V:
            if (available[cr] == False):
                break
            cr += 1
     
        
        result[u] = cr   # Assign the found color
 
        
        available = [False] * V  # Reset the values back to false for the next iteration


    if max(result) < n:
        for u in range(V):
            print("Vertex", u, " --->  Color", result[u])
    else:
        print("Cannot color")
                
           
 
# Driver Code
if __name__ == '_main_':

    v = int(input("No. of Vertices : "))
    e = int(input("No. of Edges: "))
    n = int(input("Colors : "))
     
    g1 = [[] for i in range(v)]
    for i in range (e):
        x=int(input("first Vertices : "))
        y=int(input("second Vertices : "))
        g1=addEdge(g1,x,y)
        
    '''g1 = addEdge(g1, 0, 1)
    g1 = addEdge(g1, 0, 2)
    g1 = addEdge(g1, 1, 2)
    g1 = addEdge(g1, 1, 3)
    g1 = addEdge(g1, 2, 3)
    g1 = addEdge(g1, 3, 4)'''
    print("Coloring of graph 1 ")
    greedyColoring(g1, v,n)
 
    
    '''g2 = [[] for i in range(5)]
    g2 = addEdge(g2, 0, 1)
    g2 = addEdge(g2, 0, 2)
    g2 = addEdge(g2, 1, 2)
    g2 = addEdge(g2, 1, 4)
    g2 = addEdge(g2, 2, 4)
    g2 = addEdge(g2, 4, 3)
    print("\nColoring of graph 2")
    greedyColoring(g2, 5,4)'''