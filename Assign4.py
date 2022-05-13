global N

def printSolution(board):
    for i in range(N):
        for j in range(N):
            print (board[i][j], end = " ")
        print()

def isSafe(board,i,j):
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:                #checking rows and coloumn
            return False
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):                    #checking diagonals
                if board[k][l]==1:
                    return False
    return True

def N_queen(board,n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if ( isSafe(board,i,j) and (board[i][j]!=1)):
                board[i][j] = 1
                if N_queen(board,n-1)==True:
                    return True
                board[i][j] = 0
    return False

while True:
    print ()
    N = int(input("Enter the number of queens : "))
    board = [[0 for i in range(N)]
                for j in range(N)]
    if  N_queen(board,N) == False:
        print ("Solution does not exist")
    else:
        printSolution(board)
    print("Do you want to contiue:(Y/N)")
    ch=input().lower()
    if(ch=="n"):
        break
        
'''
OUTPUT:
Enter the number of queens : 2
Solution does not exist     
Do you want to contiue:(Y/N)
y

Enter the number of queens : 4
0 1 0 0 
0 0 0 1 
1 0 0 0 
0 0 1 0 
Do you want to contiue:(Y/N)
y

Enter the number of queens : 6
0 1 0 0 0 0 
0 0 0 1 0 0 
0 0 0 0 0 1 
1 0 0 0 0 0 
0 0 1 0 0 0 
0 0 0 0 1 0 
Do you want to contiue:(Y/N)
y

Enter the number of queens : 8
1 0 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 
0 0 0 0 0 1 0 0 
0 0 1 0 0 0 0 0 
0 0 0 0 0 0 1 0
0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0
Do you want to contiue:(Y/N)
n

'''