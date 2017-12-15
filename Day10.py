# For full puzzle description please see http://adventofcode.com/2017/day/10


#=============================================================================
def run_day_10():
#
#-----------------------------------------------------------------------------
    return knot_hash_for_string("76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229")

#=============================================================================
def reverse_span(start, length, numbs):
#
# Reverse length items in the list starting at start and wrapping around 
# if required
#
#-----------------------------------------------------------------------------
    if (start + length < len(numbs)):
        numbs[start:start+length] = reversed(numbs[start:start+length])
    else :
        end_section = numbs[start : ]
        length_left = length - len(end_section)
        start_section = numbs[ : length_left]
        end_section.extend(start_section)
        end_section.reverse()
        for i in range(start, start + length):
            reversed_section_loc = i - start
            normal_section_loc = i % len(numbs)
            numbs[normal_section_loc] = end_section[reversed_section_loc]

#=============================================================================
def knot_hash_for_string(string):
#
#-----------------------------------------------------------------------------
    lengths = [ord(char) for char in string]
    lengths.extend([17, 31, 73, 47, 23])
    numbs = []
    numbs.extend(range(0, 256))
    skip_size = 0
    start = 0
    for count in range(0, 64):
        for item in lengths:
            reverse_span(start, item, numbs)
            start = start + item + skip_size
            start = start % len(numbs)
            skip_size += 1
    
    dense = dense_hash(numbs)
    hex = [format(item, 'x') for item in dense]
    result = ""

    for value in hex:
        #Preppend leading zero as required
        if len(value) == 1:
            value = "0" + value
        result = result + str(value)
    return result

#=============================================================================
def dense_hash(numbers):
#
#-----------------------------------------------------------------------------
    result = []
    for i in range(0, 16):
        value = 0
        for j in range(0, 16):
            value = value ^ numbers[i * 16 + j]
        result.append(value)
    return result