#--- Day 3: Spiral Memory ---

#You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

#Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

#17  16  15  14  13
#18   5   4   3  12
#19   6   1   2  11
#20   7   8   9  10
#21  22  23---> ...
#While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) 
#by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

#For example:

#Data from square 1 is carried 0 steps, since it's at the access port.
#Data from square 12 is carried 3 steps, such as: down, left, left.
#Data from square 23 is carried only 2 steps: up twice.
#Data from square 1024 must be carried 31 steps.
#How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

#=============================================================================
class number_with_position():
#
#-----------------------------------------------------------------------------
    #==========================================================================
    def __init__(self, number, x, y):
    #
    #--------------------------------------------------------------------------
        self.m_number = number
        self.m_x = x
        self.m_y = y
    #=============================================================================
    def distance_to_origin(self):
    #
    #-----------------------------------------------------------------------------
        return (abs(self.m_x) + abs(self.m_y))

#=============================================================================
def run_day_3():
#
#-----------------------------------------------------------------------------
    return part_2()

#=============================================================================
def part_2():
#
# We start with a massive grid of blanks then fill in our spiral
#
#-----------------------------------------------------------------------------
    grid = [[0] * 101 for __ in range(101)]

    # We want to start in the middle of the grid
    initial_position = [50, 50]
    grid[50][50] = 1
    initial_number = 1
    side_length = 1
    x_position = 51
    y_position = 50
    moving = "UP"
    side_length = 3
    moved = 0
    for num in range (1, 1000):
        value = 0
        for x in range(-1,2):
            for y in range (-1,2):
                value += grid[x_position + x][y_position + y]
        grid[x_position][y_position] = value
        if (value > 289326):
            return value
        if (moving == "UP"):
            y_position += 1
            moved += 1
            # Stop moving after we have moved up side length - 2
            if (moved == side_length - 2):
                moving = "LEFT"
                moved = 0
        elif (moving == "LEFT"):
            x_position -= 1
            moved += 1
            # Change direction when we have moved side length - 1
            if (moved == side_length - 1):
                moving = "DOWN"
                moved = 0
        elif (moving == "DOWN"):
            y_position -= 1
            moved += 1
            # Change direction when we have moved side length - 1
            if (moved == side_length - 1):
                moving = "RIGHT"
                moved = 0
        elif (moving == "RIGHT"):
            x_position += 1
            moved += 1
            # Change direction when we have moved side length
            if (moved == side_length):
                moving = "UP"
                moved = 0
                side_length += 2

#=============================================================================
def part_1():
#
# Each number is given a location based on its possition in the grid.
# We tread 1 as the origin.
# Then the distance is simple 
#
#-----------------------------------------------------------------------------

    positional_grid = []
    side_length = 1
    x_position = 0
    y_position = 0
    moving = "RIGHT"
    moved = 0
    for num in range (1, 289327):
        point = number_with_position(num, x_position, y_position)
        positional_grid.append(point)
        if (moving == "UP"):
            y_position += 1
            moved += 1
            # Stop moving after we have moved up side length - 2
            if (moved == side_length - 2):
                moving = "LEFT"
                moved = 0
        elif (moving == "LEFT"):
            x_position -= 1
            moved += 1
            # Change direction when we have moved side length - 1
            if (moved == side_length - 1):
                moving = "DOWN"
                moved = 0
        elif (moving == "DOWN"):
            y_position -= 1
            moved += 1
            # Change direction when we have moved side length - 1
            if (moved == side_length - 1):
                moving = "RIGHT"
                moved = 0
        elif (moving == "RIGHT"):
            x_position += 1
            moved += 1
            # Change direction when we have moved side length
            if (moved == side_length):
                moving = "UP"
                moved = 0
                side_length += 2

    return positional_grid[-1].distance_to_origin()


