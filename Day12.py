# For full puzzle description please see http://adventofcode.com/2017/day/12

from FileReader import read_file


#=============================================================================
def run_day_12():
#
#-----------------------------------------------------------------------------
    data = read_file("Day12_Data.txt")
    reachable = set()
    num_groups = 0
    for i in range(0, len(data)):
        if not i in reachable:
            num_groups += 1
            current_group = set()
            add_node(i, current_group, data)
            reachable = reachable | current_group
    return num_groups

#=============================================================================
def add_node(node_num, zero_connects, data):
#
# A node looks like 
# node_num <-> child_one, child_two, ..., child_n
#
#-----------------------------------------------------------------------------
    line = data[int(node_num)]
    points = line.split(" ")
    # Remove the current node and the <->, clean the commas from children
    children = [int(x.replace(",", "")) for x in points[2:]]
    for child in children:
        if not child in zero_connects:
            zero_connects.add(child)
            add_node(child, zero_connects, data)
