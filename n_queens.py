print ("Enter the number of queens")
numberOfQueen = int(input())


board = [[0]*numberOfQueen for _ in range(numberOfQueen)]

def is_attack(i, j):
    for k in range(0,numberOfQueen):
        if board[i][k]==1 or board[k][j]==1:
            return True
    for k in range(0,numberOfQueen):
        for l in range(0,numberOfQueen):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queen(n):
    if n==0:
        return True
    for i in range(0,numberOfQueen):
        for j in range(0,numberOfQueen):
           
            if (not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                
                if N_queen(n-1)==True:
                    return True
                board[i][j] = 0

    return False

N_queen(numberOfQueen)
for i in board:
    print (i)