# Collect the rows in a multidimensional list
board = [['.','.','*'], ['.','.','.'], ['.','*','.']]

# Get adjacent cells
# position is a list [0,0]
def adjacentCells(position):
    adj = []
    
    for row in range(-1, 2):
        for column in range(-1, 2):

            (newX, newY) = (position[0]+row, position[1]+column)  # adjacent cell
            
            if (newX in range(0, len(board[0]))) and (newY in range(0,len(board))) and (row, column) != (0, 0):
                adj.append([newX, newY])
    
    return adj

print(adjacentCells([0,0]))

# Check if any given spot is a mine
# input as [0,0]
def isMine(x):
    print(board[x[0]][x[1]])
    if board[x[0]][x[1]] == '*':
        True
    else:
        False

print(board[0][2])
print(isMine([0,2]))

# Iterate over every cell to check adjacent cells for mines
for column in range(len(board)):
    for row in range(len(board[column])):
        cell = [row,column]
        for mine in range(len(adjacentCells(cell))):
            continue