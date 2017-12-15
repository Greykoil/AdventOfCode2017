# For full puzzle description please see http://adventofcode.com/2017/day/11
# I am using cubic hex coordinates as described in the section at https://www.redblobgames.com/grids/hexagons/

from FileReader import read_file

#=============================================================================
def run_day_11():
#
#-----------------------------------------------------------------------------
    coord = [0,0,0]
    data = read_file("Day11_Data.txt")
    instructions = []
    for line in data:
        instructions.extend(line.split(","))
    max_dist = 0
    for move in instructions:
        if move == "n":
            coord[0] += 1
            coord[1] -= 1
        elif move == "s":
            coord[0] -= 1
            coord[1] += 1
        elif move == "ne":
            coord[2] += 1
            coord[1] -= 1
        elif move == "sw":
            coord[2] -= 1
            coord[1] += 1
        elif move == "se":
            coord[2] += 1
            coord[0] -= 1
        elif move == "nw":
            coord[2] -= 1
            coord[0] += 1
        max_dist = max(max_dist, max(abs(coord[0]), abs(coord[1]), abs(coord[2])))
    return max_dist