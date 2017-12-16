# For full puzzle description please see http://adventofcode.com/2017/day/16

#There is a cycle of length 24. IE if we repeat 24 times we get back to where
# we started

from FileReader import read_file
#=============================================================================
def run_day_16():
#
#-----------------------------------------------------------------------------
    programs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
    data = read_file("Day16_Data.txt")
    instructions = []
    for line in data:
        instructions.extend(line.split(","))
    last = 1
    seen = []
    for count in range(0, 1000000000 % 24):
        for item in instructions:
            # Spin moves the last n instructions to the front
            if item[0] == "s":
                chunk_size = item[1:]
                for i in range (0, int(chunk_size)):
                    programs.insert(0, programs.pop(-1))
            elif item[0] == "x":
                parts = item[1:].split("/")
                first = int(parts[0])
                second = int(parts[1])
                programs[first], programs[second] = programs[second], programs[first]
            elif item[0] == "p":
                first = item[1]
                second = item[3]
                a, b = programs.index(first), programs.index(second)
                programs[a], programs[b] = programs[b], programs[a]
    return programs