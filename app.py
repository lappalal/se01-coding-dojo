# Collect the rows in a multidimensional list
board = [['.','.','*',], ['.','.','.'], ['.','*','.']]
# board = [['.','.','*','.'], ['.','*','.','.'], ['.','*','.','.'], ['.','.','*','.']]

# Create the output boards based on the dimensions of the input board
width, height = len(board[0]), len(board)
counter = [[0 for x in range(width)] for y in range(height)]

# Create board shown to player
showBoard = [[' ' for x in range(width)] for y in range(height)]

# Get adjacent cells
# position is a list [0,0]
def adjacentCells(position):
    adj = []
    
    for row in range(-1, 2):
        for column in range(-1, 2):

            (newX, newY) = (position[0]+row, position[1]+column)  # adjacent cell
            
            # create list of all adjacent cells
            if (newX in range(0, len(board[0]))) and (newY in range(0,len(board))) and (row, column) != (0, 0):
                adj.append([newX, newY])
    
    return adj

# Check if any given spot is a mine
# input as [0,0]
def isMine(x):
    return board[x[0]][x[1]] == '*'

# Iterate over every cell to check adjacent cells for mines
for column in range(len(board)):
    for row in range(len(board[column])):
        cell = [row,column]

        # check for mines, if there is a mine in an adjacent field, update the counter
        for mine in range(len(adjacentCells(cell))):
            if isMine(adjacentCells(cell)[mine]) == True:
                counter[cell[0]][cell[1]] = counter[cell[0]][cell[1]] + 1

# go over counter once more to put the mines back in
for column in range(len(board)):
    for row in range(len(board[column])):
        cell = [row,column]
        if isMine(cell) == True:
            counter[cell[0]][cell[1]] = '*'

def boardShower():
    for column in range(len(showBoard)):
        print(showBoard[column])

# accept player input
#boardShower()
#move = input ("Which cell to unveil? ")
#currentMove = move.split()

print(counter)

"""
Moving forward I would compare the move input to the counter list. 
If it hits an integer, I reveal that, saving the updated board state in the showBoard list.
If the player hits a mine, they get the message "game over"
"""