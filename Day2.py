#The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. 
#For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

#For example, given the following spreadsheet:

#5 1 9 5
#7 5 3
#2 4 6 8
#The first row's largest and smallest values are 9 and 1, and their difference is 8.
#The second row's largest and smallest values are 7 and 3, and their difference is 4.
#The third row's difference is 6.
#In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.


#---Part Two---
#It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number.
# They would like you to find those numbers on each line, divide them, and add up each line's result.

from FileReader import read_file

#=============================================================================
def run_day_2():
#
#-----------------------------------------------------------------------------
    file = read_file("Day2_Data.txt")
    grid = []
    for line in file:
        str_numbers = line.split("\t")
        row = [(int(x)) for x in str_numbers]
        grid.append(row)
    return part_two(grid)

#=============================================================================
def part_two(grid):
#
#-----------------------------------------------------------------------------
    total = 0    
    for row in grid:
        for x in range(0, len(row)):
            for y in range(x+1, len(row)):
                first = row[x]
                second = row[y]
                if ((first % second) == 0):
                    total += (int)(first/second)
                elif ((second % first) == 0):
                    total +=(int)(second/first)
    return total

#=============================================================================
def part_one(grid):
#
#-----------------------------------------------------------------------------

    checksum = 0
    for row in grid:
        highest = max(row)
        lowest = min(row)
        diff = highest - lowest
        checksum += diff;
    return checksum