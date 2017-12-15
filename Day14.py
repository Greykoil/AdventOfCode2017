# For full puzzle description please see http://adventofcode.com/2017/day/15

from Day10 import knot_hash_for_string

#=============================================================================
def run_day_14():
#
#-----------------------------------------------------------------------------
    key_string = "ugkiagan"
    line_strings = []
    for i in range(0, 128):
        line_strings.append(key_string + "-" + str(i))
    
    # Get the hash from day 10
    hash_strings = [knot_hash_for_string(x) for x in line_strings]

    binary_strings = []
    scale = 16
    num_of_bits = 128
    for item in hash_strings:
        binary_rep = bin(int(item, scale))[2:].zfill(num_of_bits)
        binary_strings.append(binary_rep)


    binary_squares = []

    for line in binary_strings:
        strip = []
        for char in line:
            if char == "1":
                strip.append(1)
            else :
                strip.append(0)
        binary_squares.append(strip)
    regions = 0
    for x_loc in range(0, len(binary_squares)):
        for y_loc in range(0, len(binary_squares)):
            if binary_squares[x_loc][y_loc] == 1:
                regions += 1
                binary_squares[x_loc][y_loc] = 0
                change_adjacent_squares(x_loc, y_loc, binary_squares)
    return regions

#=============================================================================
def change_adjacent_squares(x_loc, y_loc, binary_squares):
#
#-----------------------------------------------------------------------------
    if (x_loc > 0 and binary_squares[x_loc-1][y_loc]):
        binary_squares[x_loc - 1][y_loc] = 0
        change_adjacent_squares(x_loc - 1, y_loc, binary_squares)
    if (x_loc < len(binary_squares) -1 and binary_squares[x_loc + 1][y_loc]):
        binary_squares[x_loc + 1][y_loc] = 0
        change_adjacent_squares(x_loc + 1, y_loc, binary_squares)
    if (y_loc > 0 and binary_squares[x_loc][y_loc - 1]):
        binary_squares[x_loc][y_loc - 1] = 0
        change_adjacent_squares(x_loc, y_loc - 1, binary_squares)
    if (y_loc < len(binary_squares) -1 and binary_squares[x_loc][y_loc + 1]):
        binary_squares[x_loc][y_loc + 1] = 0
        change_adjacent_squares(x_loc, y_loc + 1, binary_squares)
        

