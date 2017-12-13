# For full puzzle description please see http://adventofcode.com/2017/day/13

from FileReader import read_file

#=============================================================================
class scanner():
#
#-----------------------------------------------------------------------------
    #=============================================================================
    def __init__(self):
    #
    #-----------------------------------------------------------------------------
        self.m_depth = 0
        self.m_decending = True
        self.m_position = -1
    #=============================================================================
    def zero_on_turn(self, turn):
    #
    # A scanner is at 0 if it is turn 0 or a multiple of 2(depth-1)
    #
    #-----------------------------------------------------------------------------
        if (self.m_depth == 0):
            return False
        else :
            return (turn % (2*(self.m_depth - 1)) ==0)
        


#=============================================================================
def run_day_13():
#
#-----------------------------------------------------------------------------
    data = read_file("Day13_Data.txt")
    
    # find the deepest layer that we need
    deepest = -1
    bits = data[-1].split(": ")
    deepest = int(bits[0])
    # set up our vector of depth / location pairs
    scanners = []
    for i in range (0, deepest + 1):
        scanners.append(scanner())
    
    for line in data:
        bits = line.split(": ")
        # Get the information out of the file line
        level = int(bits[0].strip())
        depth = int(bits[1].strip())

        # Set the depth and initial position for the scanner
        scanners[level].m_depth = depth
        scanners[level].m_position = 0
    delay = 0
    while (True):
        if (pass_scanners(scanners, delay)):
            return delay
        delay += 1

#=============================================================================
def pass_scanners(scanners, start_time):
#
#-----------------------------------------------------------------------------
    for i in range(0, len(scanners)):
        time = start_time + i
        if scanners[i].zero_on_turn(time):
            return False
    return True