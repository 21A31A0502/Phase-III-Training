


def isPossible(board, x, y, value):
    # Same row checking 
    for col in range(9):
        if board[x][col] == str(value):
            return False
    
    # Same col checking
    for row in range(9):
        if board[row][y] == str(value):
            return False
    
    # Same 3 * 3 matrix checking 
    topRow = (row // 3) * 3 
    topCol = (col // 3) * 3 
    
    for i in range(3):
        for j in range(3):
            if board[topRow + i][topCol + j] == str(value):
                return False
    return True





def printMatrix(x, y, board):
    if x == 9:
        return True
    
    nextX, nextY = -1, -1 
    
    if y == 8:
        nextX = x + 1 
        nextY = 0 
    else:
        nextX = x 
        nextY = y + 1
        
    if board[x][y] != ".":
        return printMatrix(nextX, nextY, board)
        
        
    for value in range(1, 10):
        if isPossible(board, x, y, value):
            board[x][y] = str(value)
            result = printMatrix(nextX, nextY, board)
            if result == True:
                return True
            board[x][y] = "."
                
    return False
    

board = []
for i in range(9):
    row = []
    for j in range(1, 10):
        row.append(j)
    board.append(row)

printMatrix(0, 0, board)