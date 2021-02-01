# Question 5 (%30)

# Assume a maze is given by an array of arrays:

maze1 = [[0, 1, 1, 1, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 1, 0, 0],
         [1, 1, 0, 1, 0, 0, 1, 0],
         [1, 0, 0, 0, 1, 0, 1, 0],
         [0, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 1, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 0, 1, 0]]

# The cells that contain 0 are passable, and the cells with 1 are
# walls. A person starting at maze[0][0] (top left) can move up, down,
# left, or right but only to other pssable cells. The question is whether
# the maze can be solved. Assume the goal is to get to the bottom right
# corner (e.g. maze[7][7]. maze1 given above is solvable, since there is
# a path from the top left to the bottom right.

# As another example, maze2 below is not solvable (there is no path from
# the top left to the bottom right):  

maze2 = [[0, 1, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 1, 0, 1, 0, 1],
         [1, 1, 0, 1, 0, 1, 0, 0],
         [1, 1, 0, 1, 0, 0, 0, 1],
         [1, 0, 0, 0, 0, 1, 1, 1],
         [0, 0, 1, 0, 0, 1, 1, 1],
         [0, 1, 1, 0, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 1, 0, 0]]

# Complete the function below, which takes a 2D maze array, a starting
# point, and an end point (goal). The function should return True if the
# maze is solvable, and False if not. The player can only move up, down,
# left, right; they cannot pass through walls and cannot move past the
# edges of the maze.

# The function should be able to work with any size maze. Start and goal
# locations are given as tuples of the form (x,y). Your function is allowed # to mark the maze array if necessary (Hint: think Hansel and Gretel :).
solved = False

def is_solvable(maze, start, goal):
    x_current = int(start[0])
    y_current = int(start[1])
    width = len(maze[0])
    length = len(maze[1])

    #print((x_current, y_current))

    if (x_current < 0 or y_current < 0): #out of range in the beginning
        return
    if(x_current > width - 1 or y_current > length - 1): #out of range in the x,y coordinates
        return
    if (maze[x_current][y_current] == 1): #wall
        return
    if (maze[x_current][y_current] == '*'): #bread crumbs
        return
    if ((x_current, y_current) == goal):
        #print the array when reached the goal
        for i in maze:
            for j in i:
                print(str(j) + " ", end="")
            print("")
        solved = True
        print(solved)
        exit(0)  #exit the program when reached the goal

    maze[x_current][y_current] = '*'
    is_solvable(maze, (x_current, y_current + 1), goal)  # down
    is_solvable(maze, (x_current, y_current - 1), goal)  # up
    is_solvable(maze, (x_current + 1, y_current), goal)  # left
    is_solvable(maze, (x_current - 1, y_current), goal)  # right


# The following should work correctly:

print(is_solvable(maze1, (0,0), (7,7)))
# should print True

print(is_solvable(maze2, (0,0), (7,7)))
if solved == False:
    print('False')
# should print False
