class Node:
    def __init__(self,data,level,fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up,down,left,right} """
        x,y = self.find(self.data,'_')
        """ val_list contains position values for moving the blank space in either of
            the 4 directions [up,down,left,right] respectively. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
        return children
        
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Move the blank space in the given direction and if the position value are out
            of limits the return None """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
            

    def copy(self,root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self,puz,x):
        """ Specifically used to find the position of the blank space """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j




""" Initialize the puzzle size by the specified open and closed lists to empty """
open = []
closed = []


def f(start,goal):
        """ Heuristic Function to calculate hueristic value f(x) = h(x) + g(x) """
        return h(start.data,goal)+start.level

def h(start,goal):
        """ Calculates the difference between the given puzzles """
        temp = 0
        for i in range(0,3):
            for j in range(0,3):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
        

def Astar(start,goal):
        start = Node(start,0,0)
        start.fval = f(start,goal)
        """ Put the start node in the open list"""
        open.append(start)
        print("")
        while True:
            cur = open[0]
            print("")
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            print("\nH score :",(cur.fval-cur.level))
            print("G score : ",cur.level)
            print("F score : ", cur.fval)
            print("\n=====================================")

           
            if(h(cur.data,goal) == 0):
                break
            for i in cur.generate_child():
                i.fval = f(i,goal)
                open.append(i)
            closed.append(cur)
            del open[0]

            """ sort the opne list based on f value """
            open.sort(key = lambda x:x.fval,reverse=False)

start=[[1,2,3],['_',4,6],[7,5,8]]
goal=[[1,2,3],[4,5,6],[7,8,'_']]
print("Solve : ")
Astar(start,goal)

'''
Solve : 



  | 
  | 
 \'/ 

1 2 3 
_ 4 6 
7 5 8 

H score : 3
G score :  0
F score :  3

=====================================


  | 
  | 
 \'/ 

1 2 3 
4 _ 6
7 5 8

H score : 2
G score :  1
F score :  3

=====================================


  |
  |
 \'/

1 2 3
4 5 6
7 _ 8

H score : 1
G score :  2
F score :  3

=====================================


  |
  |
 \'/

1 2 3
4 5 6
7 8 _

H score : 0
G score :  3
F score :  3

=====================================
'''