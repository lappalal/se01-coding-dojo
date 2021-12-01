# Collect the rows in a multidimensional list
board = [['.','.','*'], ['.','.','.'], ['.','*','.']]

# Get adjacent cells
def adjacentCells(position):
    adj = []
    
    for row in range(-1, 2):
        for column in range(-1, 2):

            (newX, newY) = (position[0]+row, position[1]+column)  # adjacent cell
            
            if (newX in range(0, len(board[0]))) and (newY in range(0,len(board))) and (row, column) != (0, 0):
                adj.append((newX, newY))
    
    return adj

# Check if any given spot is a mine
def isMine(spot):
    if spot == '*':
        True
    else:
        False

# Iterate over every cell to check adjacent cells for mines
for column in range(len(board)):
    for row in range(len(board[column])):
        cell = [row,column]
        #print(adjacentCells(cell))
        for mine in range(len(adjacentCells(cell))):
            if isMine(adjacentCells(cell)[mine]) == True:
                print(cell)