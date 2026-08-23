import numpy as np
import matplotlib.pyplot as plt
import math

############## Variables ################

wrap_boundary = True
n = 30 # n^2 board
runtime = 9999
timestep = 1 # how often to print the board
probability = 10 # alive cell probability in initial seed
alive_cells = [(13,13), (13,14), (14, 15), (14,13), (15,13), (14,15)] # for manual board setup

#########################################

board = np.zeros((n, n)) # create board

############# Initial Board #############

##### manual setup
#for cell in alive_cells:
#    board[cell] = 1

##### auto-random setup
for i in range(board.shape[0]):
    for j in range(board.shape[1]):
        if np.random.rand() < probability/100:
            board[i,j] = 1

#########################################

# inital board png
plt.imshow(board)
plt.savefig("board0.png")
plt.close()
print("Done: board0.png")


test2_board = board.copy()

for t in range(runtime):
    try:
        test2_board = test_board.copy() # for checking alternate steady state
    except:
        pass
    test_board = board.copy() # for checking steady states
    temp_board = board.copy() # for updating board
    for y in range(n): # iterates across board
        for x in range(n):
            nbr = 0 # initialise empty neighbour values
            x2 = x - 1 
            while x2 < x + 2: # iterates through surrounding x's and y's for current cell
                y2 = y - 1
                while y2 < y + 2:
                    if y2 != y or x2 != x: # doesn't count current cell
                        
                        if wrap_boundary: # boundary condition - wrap
                            nbr += board[y2 % n,x2 % n]
                        else: # boundary condition - no wrap
                            try:
                                if x2 != -1 and y2 != -1:
                                    nbr += board[y2,x2] # sums neighbour values
                            except IndexError:
                                pass

                    y2 += 1
                x2 += 1
            if board[y,x] == 1:
                if not(nbr == 2 or nbr == 3): # kills cell if nbr is too low/high
                    temp_board[y,x] = 0
            elif nbr == 3: # brings dead cell back to life if there are 3 neighbours
                temp_board[y,x] = 1
    
    board = temp_board.copy() # update actual board
    
    if np.array_equal(test_board,board): # checks for steady state
        plt.imshow(board)
        plt.savefig(f"board{t+1:05d}-steadystate.png")
        print(f"Done: board{t+1:05d}-steadystate.png")
        print("Steady State Found")
        exit()
    elif np.array_equal(test2_board,board): # checks for alternating steady state
        plt.imshow(board)
        plt.savefig(f"board{t+1:05d}-Asteadystate.png")
        print(f"Done: board{t+1:05d}-Asteadystate.png")
        print("Alternating Steady State Found")
        exit() 
    elif math.floor((t+1)/timestep) == (t+1)/timestep: # prints board at timesteps
        plt.imshow(board)
        plt.savefig(f"board{t+1:05d}.png")
        plt.close()
        print(f"Done: board{t+1:05d}.png")
