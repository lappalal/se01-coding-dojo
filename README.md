# se01-coding-dojo
Coding Assessment at CODE University of Applied Sciences

# Explaining the code

First we take a board as input. This input is in the form of a multidimensional list.

We then create 2 new boards, based on the input dimensions. One is filled with zeros, the other is "empty" (filled with spaces).

## Functions
### `adjacentCells(position)`
takes a position as list `[x,y]`.
returns all cells adjacent to the input cells as list `[[x1,y1][x2,y2]]`

### `isMine`
takes a position as list `[x,y]`.
returns boolean if the cell has a mine (`*`) in it.

### `boardShower`
takes no inputs.
returns showBoard, an empty board meant to show player input.

# Usage
The software currently returns the amount of mines in any adjacent fields based on the board input.

Moving forward a player sees an empty board, and is allowed to input moves as coordinates (x,y). These coordinates are checked against the `counter` list to see how many mines are adjacent to the field the player input. This number ist then updated in `showBoard` and a complete board is shown to the player again.

if the player hits a mine the game ends.

if the player hits a 0, the code should check all adjacent cells and return any integers into the `showBoard`. once again a full board is shown to the player.