# selection sort 
from collections import defaultdict


def selectionsort(arr):

    n= len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):

            if arr[min]>arr[j]:
                min=j
        
        arr[i],arr[min]=arr[min],arr[i]
    
    print("Sorted : ", arr)

# BFS DFS =================================
class Graph:
    def __init__(self,v,e) :
        self.adj=defaultdict(list)
        self.v=v
        self.e=e
    def add(self,s,d):
        self.adj[s].append(d)
        self.adj[d].append(s)

    def print_g(self):
        for i in range(self.v):
            print(i,"-->", self.adj[i])
    
    def bfs(self,s):
        visit=[False]*self.v
        queue=[]
        visit[s]=True
        queue.append(s)
        print("BFS---> ")
        while queue:
            v=queue.pop(0)
            print(v,end=" ")
            for i in self.adj[v]:
                if visit[i]==False:
                    visit[i]=True
                    queue.append(i)


    # rec dfs 
    def dfsu(self,s):
        visit=[False]*self.v
        print("\nDFS---> ")
        self.dfs(visit,s)
    
    def dfs(self,visit,s):

        visit[s]=True
        print(s,end=" ")

        for i in self.adj[s]:
            if visit[i]==False:
                self.dfs(visit,i)

    # non rec dfs
    def dfsn(self,s):
        visit=[False]*self.v
        print("\nDFS non rec ---> ")
        visit[s]=True
        stack=[]
        stack.append(s)
        while stack:
            v=stack.pop()
            print(v,end=" ")
            for i in self.adj[v]:
                if visit[i]==False:
                    stack.append(i)
                    visit[i]=True

# N queen back track========================================== 
def Print_board(board,N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def isSafe(board,r,c,N):
    # check row n col
    for  k in range(N):
        if board[r][k]==1 or board[k][c]==1:
            return False
    # check diagonal
    i,j=r,c
    while(i>=0 and j>=0) :  # left upper diagonal
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    i,j=r,c
    while (j>=0 and i<N):  # right upper diagonal 
        if board[i][j]==1:
            return False
        j-=1
        i+=1

    return True
    """ Python3 program to solve N Queen Problem
using Branch or Bound """

N = 8

""" A utility function to print solution """
def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()

""" A Optimized function to check if
a queen can be placed on board[row][col] """
def isSafe(r, c, 
		rowLookup, slashCodeLookup,
					backslashCodeLookup):
	if (slashCodeLookup[r+c] or
		backslashCodeLookup[(r-c+N-1)] or
		rowLookup[r]):
		return False
	return True

""" A recursive utility function
to solve N Queen problem """
def solveNQueensUtil(board, col, 
					rowLookup, slashCodeLookup,
					backslashCodeLookup):
						
	""" base case: If all queens are
	placed then return True """
	if(col >= N):
		return True
	for i in range(N):
		if(isSafe(i, col,
				rowLookup, slashCodeLookup,
				backslashCodeLookup)):
					
			""" Place this queen in board[i][col] """
			board[i][col] = 1
			rowLookup[i] = True
			slashCodeLookup[i+col] = True
			backslashCodeLookup[i-col+N-1] = True
			
			""" recur to place rest of the queens """
			if(solveNQueensUtil(board, col + 1,
								
								rowLookup, slashCodeLookup,
								backslashCodeLookup)):
				return True
			
			""" If placing queen in board[i][col]
			doesn't lead to a solution,then backtrack """
			
			""" Remove queen from board[i][col] """
			board[i][col] = 0
			rowLookup[i] = False
			slashCodeLookup[i+col] = False
			backslashCodeLookup[i-col+N-1] = False
			
	""" If queen can not be place in any row in
	this column col then return False """
	return False

""" This function solves the N Queen problem using
Branch or Bound. It mainly uses solveNQueensUtil()to
solve the problem. It returns False if queens
cannot be placed,otherwise return True or
prints placement of queens in the form of 1s.
Please note that there may be more than one
solutions,this function prints one of the
feasible solutions."""
def solveNQueens():
	board = [[0 for i in range(N)]
				for j in range(N)]
	
	# helper matrices
	slashCode = [[0 for i in range(N)]
					for j in range(N)]
	backslashCode = [[0 for i in range(N)]
						for j in range(N)]
	
	# arrays to tell us which rows are occupied
	rowLookup = [False] * N
	
	# keep two arrays to tell us
	# which diagonals are occupied
	x = 2 * N - 1
	slashCodeLookup = [False] * x
	backslashCodeLookup = [False] * x
	
# 	# initialize helper matrices
# 	for rr in range(N):
# 		for cc in range(N):
# 			slashCode[rr][cc] = rr + cc
# 			backslashCode[rr][cc] = rr - cc + 7
	
	if(solveNQueensUtil(board, 0,
						rowLookup, slashCodeLookup,
						backslashCodeLookup) == False):
		print("Solution does not exist")
		return False
		
	# solution found
	printSolution(board)
	return True

# Driver Cde
solveNQueens()

# This code is contributed by SHUBHAMSINGH10

def isSafe(board,r,c,N):
    for k in range(0,N):
        if board[r][k]==1 or board[k][c]==1:                #checking rows and coloumn
            return False
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==r+c) or (k-l==r-c):                    #checking diagonals
                if board[k][l]==1:
                    return False
    return True
    
def Solution_Nqueen(board,col,N):
    if col>=N:
        return True
    for i in range(0,N):
        #for j in range(0,N):
            if(isSafe(board,i,col,N)==True and board[i][col]!=1):
                board[i][col]=1
                if Solution_Nqueen(board,col+1,N)==True:
                    return True
                board[i][col]=0 # backtrack
    
    return False # no solution 
# astar =====================================
# a star 
class Node :
    def __init__(self,mat,f,g):
        self.mat=mat
        self.f=f  
        self.g=g
    
    def print_mat(self):
        for i in self.mat:
            for j in i:
                print(j,end=" ")
            print()
            
    def find(self,x) :
        for i in range(len(self.mat)):
            for j in range(len(self.mat)):
                if self.mat[i][j]==x:
                    return i,j
    
    def copy(self):
        copy=[]
        for i in (self.mat):
            t=[]
            for j in i:
                t.append(j)
            copy.append(t)
                
        return copy
                
        
    def position_mat(self,x1,y1,x2,y2):
        
        if(x2>=0 and x2<len(self.mat) and y2>=0 and y2<len(self.mat)):
            temp_mat=[]
            temp_mat=self.copy()
            temp_mat[x1][y1],temp_mat[x2][y2]=temp_mat[x2][y2],temp_mat[x1][y1]
            return temp_mat
        else:
            return None 
        
        
    def generate_child(self):
        
        x1,y1=self.find('_')
        
        # actions =[up,down,left,right]
        actions=[[x1,y1-1],[x1,y1+1],[x1-1,y1],[x1+1,y1]]
        children =[]
        for i in actions:
           
            child = self.position_mat(x1,y1,i[0],i[1])
            if child is not None:
                child_node=Node(child,0,self.g+1)
                children.append(child_node)
                
        return children
    
    
def f(mat,goal,g):
    return h(mat,goal)+g 
    
def h(mat,goal):
    mis=0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]!=goal[i][j] and mat[i][j] != '_':
                mis+=1 
    
    return mis 
    
  
def Astar(start,goal):
    openl=[]
    close=[] 
    s=Node(start,0,0)
    s.f=f(s.mat,goal,s.g)
    
    openl.append(s)
    
    while True:
        n= openl[0]
        #n=min(openl,key=lambda x:x.f)
        print("\n select")
        n.print_mat()
        print()
        print("F-value : ",n.f)
        print("H-value : ",n.f-n.g)
        print("G-value: ",n.g)
        print("========================")
        if h(n.mat,goal)==0:
            break 
        
        child_list=n.generate_child()
        print("Intermediate solutions")
        for i in child_list:
          
                i.f=f(i.mat,goal,i.g)
                i.print_mat()
                print()
                print("F-value : ",i.f,end=" ")
                print("\tH-value : ",i.f-i.g,end=" ")
                print("\tG-value: ",i.g)
                
                openl.append(i)
        print("=============================")
        close.append(n)
        del openl[0]
        openl.sort(key=lambda x:x.f,reverse=False) # asecending order

def menu():
    while True:
        ch=int(input("ch: "))
        if ch==1:
            g=Graph(7,11)
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
            g.print_g()
            g.bfs(0)
            g.dfsu(0)
            g.dfsn(0)

        if ch==2:
            arr=[76,34,21,2,1,98,32,17,23,11,29]
            print(arr)
            selectionsort(arr)
        if ch==3:
            while True:
                N=int(input("Q : "))
                board=[[0]*N for _ in range(N)]
                if Solution_Nqueen(board,0,N) == True:
                    Print_board(board,N)
                else:
                    print("No sol")
                
                y=int(input("0/1"))
                if y==1:
                    break
        
        if ch==4:
                    
            start =[[1,2,3],['_',4,6],[7,5,8]]
            goal =[[1,2,3],[4,5,6],[7,8,'_']]

            # s.print_mat()
            # v=s.generate_child()
            # for i in v:
            #     print()
            #     i.print_mat()
            Astar(start,goal)
        if ch==5:
            pass
        if ch ==6:
            pass 
        if ch==7:
            break
        


menu()


    