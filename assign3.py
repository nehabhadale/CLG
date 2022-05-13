'''  graph
        2   3
    (0)--(1)--(2)
    |   / \   |
   6| 8/   \5 |7
    | /     \ |
    (3)-------(4)
        9     '''

class Graph(object):
    def __init__(self, vertices):
        self.vertices = vertices                        
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]       

    def getMinimumKey(self, weight, visited):
     
        min = 9999

        for i in range(self.vertices):
           
            if weight[i] < min and visited[i] == False:
                min = weight[i]
                minIndex = i

       
        return minIndex

    def primsAlgo(self):
        weight = [9999] * self.vertices    
        MST = [None] * self.vertices       
        weight[0] = 0                       
        visited = [False] * self.vertices
        MST[0] = -1                        

        for i in range(self.vertices):
            minIndex = self.getMinimumKey(weight, visited)
           
            visited[minIndex] = True

            for vertex in range(self.vertices):
                if self.graph[minIndex][vertex] > 0 and visited[vertex] == False and \
                weight[vertex] > self.graph[minIndex][vertex]:
                    weight[vertex] = self.graph[minIndex][vertex]
                    MST[vertex] = minIndex

        self.printMST(MST)

    def printMST(self, MST):
        print ("Edge \tWeight")
        tcost=0
        for i in range(1, self.vertices):
            print (MST[i],"-",i,"\t",self.graph[i][ MST[i] ])
            tcost+=self.graph[i][ MST[i] ]
        print("Total cost of minimum spanning tree : ",tcost)


g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
 
g.primsAlgo()

''' 
====OUTPUT======
Edge    Weight
0 - 1    2
1 - 2    3
0 - 3    6
1 - 4    5
Total cost of minimum spanning tree :  16
'''
