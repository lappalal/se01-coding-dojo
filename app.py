# Get Board input in different rows
boardRowOne = input('Please enter the first row of the board: ')
boardRowTwo = input('Please enter the second row of the board: ')
boardRowThree = input('Please enter the third row of the board: ')

# Collect the rows in a multidimensional array
board = [boardRowOne.split(), boardRowTwo.split(), boardRowThree.split()]


# Check if any given spot is a mine
def isMine(spot):
    if spot == '*':
        return True
    else:
        False

# Iterate over every spot on the board
for row in range(len(board)):
    for spot in range(len(board[row])):
        print(spot)

        # Take the first spot in every row and check the field left of it
        if spot == 0:
            print(spot)
            if isMine(spot) == True:
                print('Is Mine!')
            else:
                print('Not Mine!')