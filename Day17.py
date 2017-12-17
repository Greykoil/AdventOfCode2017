# For full puzzle description please see http://adventofcode.com/2017/day/16

#=============================================================================
def run_day_17():
#
#-----------------------------------------------------------------------------
    buffer = [0]

    position = 0
    step = 363
    length = 1
    following_zero = -1
    last = 1
    for i in range(1, 50000000):
        new_position = ((position + step) % length) + 1
        if (new_position == 1):
            following_zero = i
        position = new_position
        length += 1

        if (i > last * 2):
            print(last)
            last = last * 2

    return following_zero
