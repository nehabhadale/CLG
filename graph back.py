class Graph():
 
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
 
    # check if safe to colour
    def canColorVertex(self, v, colour, c):
        for i in range(self.vertices):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
    


    def vertexColor(self, m, colour, v):
        #if all vertices are coloured return True
        if v == self.vertices:
            return True
 
        #check for different color options for vertices
        for c in range(1, m + 1):
            if self.canColorVertex(v, colour, c) == True:
                colour[v] = c
                #recursive call for coloring other vertices
                if self.vertexColor(m, colour, v + 1) == True:
                    return True
                colour[v] = 0
        return False
 

    def colorGraph(self, m):
        colour = [0] * self.vertices
        if self.vertexColor(m, colour, 0) == False:
           print("Cannot color...Solution doesnt exist!")
        else:
        # Print the solution
            print ("Colors used :")
            for c in colour:
                print (c,end=' ')
        

# Driver Code
n = int(input("No. of Vertices : "))
m = int(input("Colors : "))
g = Graph(n)

print("Vertices : ")
for i in range (n):
    l = []
    for j in range (n):
        x = int(input())
        l.append(x)
    g.graph.append(l)

# g.printGraph()
g.colorGraph(m)

# [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
