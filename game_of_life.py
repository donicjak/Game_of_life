"""
Homework 01 - Game of life.

Your task is to implement a kind of cellular automaton called "Game of life".
The automaton is a 2D simulation where each cell on the grid is either dead
or alive.

The state of each cell is updated in every iteration based state of neighbouring cells.
Cell neighbours are cells that are horizontally, vertically, or diagonally adjacent.

Rules for the update are as follows:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.


Our implementation uses the coordinate system with grid coordinates starting
from (0, 0) - upper left corner. The first coordinate is a row, and the second
is a column.

Do not use wrap-around (toroid) when reaching the edge of the board.

For more details about Game of Life, see Wikipedia:
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""


def update(alive: set, size: (int, int), iter_n: int) -> set:
    """
    Perform iter_n iterations.

    Args
    ----
        alive (set):
            A set of cell coordinates marked as alive, can be empty.
        size (int, int):
            The size of simulation grid as a tuple of two ints.
        iter_n (int):
            A number of iterations to perform.

    Returns
    -------
        _  (set):
            A set of coordinates of alive cells after iter_n iterations.
    """
    # TODO: Implement update rules.


    next_gen = set()
    current_gen = set(alive)

    for i in range(iter_n):
        if ( i != 0):
            #print("PROBIHA ITERACE JINA NEZ 0")
            current_gen = set(next_gen)
            next_gen = set()
        
        for row in range(size[0]):
            for collum in range(size[1]):         
                if((row, collum) in current_gen):
                    #print("Cell on position (",row, ",", collum,") is alive")
                
                    #print("Divame se na sousedy:")
                    live_neighbours = 0
                    if ( (row-1,collum-1) in current_gen):
                        #print(row-1, collum-1, "je nazivu")
                        live_neighbours += 1
                    #else:
                        #print(row-1, collum-1, "neni nazivu")
                    if ((row-1,collum) in current_gen):
                       # print(row-1, collum, "je nazivu")
                        live_neighbours += 1

                   # else:
                       # print(row-1, collum, "neni nazivu")
                    if ((row-1,collum+1) in current_gen):
                        #print(row-1, collum+1, "je nazivu")
                        live_neighbours += 1
                    #else:
                        #print(row-1, collum+1, "neni nazivu")
                    if ((row,collum-1) in current_gen):
                        #print(row, collum-1, "je nazivu")
                        live_neighbours += 1
                   # else:
                        #print(row, collum-1, "neni nazivu")
                    if ((row,collum+1) in current_gen):
                       # print(row, collum+1, "je nazivu")
                        live_neighbours += 1
                    #else:
                        #print(row, collum+1, "neni nazivu")
                    if ((row+1,collum-1) in current_gen):
                       # print(row+1, collum-1, "je nazivu")
                        live_neighbours += 1
                   # else:
                       # print(row+1, collum-1, "neni nazivu")
                    if ((row+1,collum) in current_gen):
                       # print(row+1, collum, "je nazivu")
                        live_neighbours += 1
                    #else:
                       # print(row+1, collum, "neni nazivu")
                    if ((row+1,collum+1) in current_gen):
                        #print(row+1, collum+1, "je nazivu")
                        live_neighbours += 1
                    #else:
                        #print(row+1, collum+1, "neni nazivu")

                    #print("Na zivu je ", live_neighbours, "sousedu")
                    if (live_neighbours == 2 or live_neighbours == 3):
                        #print("Cell is staying alive")
                        next_gen.add((row, collum))
                   # else:
                        #print("Cell is dying")
                else:
                    #print("Cell on position (",row, ",", collum,") is dead")

                    #print("Divame se na sousedy:")
                    live_neighbours = 0
                    if ( (row-1,collum-1) in current_gen):
                       # print(row-1, collum-1, "je nazivu")
                        live_neighbours += 1
                   # else:
                      #  print(row-1, collum-1, "neni nazivu")
                    if ((row-1,collum) in current_gen):
                       # print(row-1, collum, "je nazivu")
                        live_neighbours += 1

                    #else:
                        #print(row-1, collum, "neni nazivu")
                    if ((row-1,collum+1) in current_gen):
                       # print(row-1, collum+1, "je nazivu")
                        live_neighbours += 1
                    #else:
                        #print(row-1, collum+1, "neni nazivu")
                    if ((row,collum-1) in current_gen):
                       # print(row, collum-1, "je nazivu")
                        live_neighbours += 1
                   # else:
                        #print(row, collum-1, "neni nazivu")
                    if ((row,collum+1) in current_gen):
                        #print(row, collum+1, "je nazivu")
                        live_neighbours += 1
                    #else:
                       # print(row, collum+1, "neni nazivu")
                    if ((row+1,collum-1) in current_gen):
                      #  print(row+1, collum-1, "je nazivu")
                        live_neighbours += 1
                   # else:
                       # print(row+1, collum-1, "neni nazivu")
                    if ((row+1,collum) in current_gen):
                      #  print(row+1, collum, "je nazivu")
                        live_neighbours += 1
                    #else:
                       # print(row+1, collum, "neni nazivu")
                    if ((row+1,collum+1) in current_gen):
                       # print(row+1, collum+1, "je nazivu")
                        live_neighbours += 1
                    #else:
                       # print(row+1, collum+1, "neni nazivu")

                   # print("Na zivu je ", live_neighbours, "sousedu")
                    if (live_neighbours == 3 ):
                        #print("Cell is going alive")
                        next_gen.add((row, collum))
                   # else:
                       # print("Cell is staying dead")


        
            


    
   # print("end is near") 
    #print("dalsi generace je:", next_gen)       
    return next_gen


def draw(alive: set, size: (int, int)) -> str:
    """
    Draw a game board.  

    Args
    ----
        alive (set):
            A set of cell coordinates marked as alive, can be empty.
        size (int, int):()
    -------
        _  (string):
           A string showing the board state with alive cells marked with X.
    """
    # TODO: implement board drawing logic and return it as output
    # Don't call print in this method, just return board string as output.
    # Example of 3x3 board with 1 alive cell at coordinates (0, 2):
    # +---+
    # |  X|
    # |   |
    # |   |
    # +---+

    #print("Mapa o rozmerech:", size[0] ,"x", size[1], "ale musime ji udelat vetsi a sice ",size[0]+ 2, "x",size[1]+2)
   # print("Mame X na pozicich:", alive, "ale potrebujeme je na pozicih o jedna vysssi")

    drawing = [[0 for c in range(size[1]+2)] for r in range(size[0]+2)]
    
   # print(drawing)
    for row in range(size[0]+2):
     #   print("novy radek")
        for collum in range(size[1]+2):
            if(row == 0 or row == (size[0]+1)):
                if (collum == 0 or collum == (size[1]+1)):
                    drawing[row][collum] = '+'
                  #  print("+")
                else:
                   # print("-")
                    drawing[row][collum] = '-'

            elif(row != (size[0]+1)  ):
                if(( collum == 0 or collum == (size[1]+1))):
                 #   print("|")
                    drawing[row][collum] = '|'
                elif((row-1,collum-1) in alive):
                  #  print("X")
                    drawing[row][collum] = 'X'
                else:
                   # print("0")
                    drawing[row][collum] = ' '


    retezec = ""
    for i in range(size[0]+2):
        if (i != 0 ):
            retezec += '\n'
        for j in range(size[1]+2):
            retezec += drawing[i][j]
            
    
    #print(retezec)

    return retezec


