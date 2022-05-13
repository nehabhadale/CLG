from collections import defaultdict
class Node:
    def __init__(self,v,e):
        self.adj= defaultdict(list)
        self.v=v
        self.e=e
        
    def add(self,s,d):
        self.adj[s].append(d)
        self.adj[d].append(s)
    
    def print_l(self):
        for i in range(self.v):
            print(i , "--> ",self.adj[i])
    
    
    def bfs(self,s):
        visit=[False]*(self.v)
        
        queue=[]
        queue.append(s)
        visit[s]=True
       
        while(queue):
            
            s = queue.pop(0)
           
           
            print(s,end=" ")
           
            for i in self.adj[s]:
                if visit[i]==False:
                    #print(i)
                    queue.append(i)
                    visit[i]=True
                
    def dfs(self,visited,s) :
        visited[s]=True
        print(s,end=' ')
        for i in self.adj[s]:
            if visited[i]==False:
                self.dfs(visited,i)
                
    def duitl(self,s):
        visited=[False]*self.v
        print()
        self.dfs(visited,s)
        
            
    
v=7  
e=11
g= Node(v,e)
# for i in range(e):
#         s=int(input("sorce"))
#         d=int(input("dest"))
#         g.add(s,d)

g.add(0,1)
g.add(1,2)        
g.add(0,3)        
g.add(1,3)  
g.add(2,3) 
g.add(2,4) 
g.add(2,5) 
g.add(1,5)
g.add(1,6) 
g.add(3,4)
g.add(4,6) 
g.print_l()
g.bfs(0)
g.duitl(0)

        
    
    
    
    
        
        
        
