#--- Day 8: I Heard You Like Registers ---

#You receive a signal directly from the CPU. Because of your recent assistance with jump instructions, it would like you to compute the result of a series of unusual register instructions.

#Each instruction consists of several parts: the register to modify, whether to increase or decrease that register's value, 
#the amount by which to increase or decrease it, and a condition. If the condition fails, skip the instruction without modifying the register. 
#The registers all start at 0. The instructions look like this:

#b inc 5 if a > 1
#a inc 1 if b < 5
#c dec -10 if a >= 1
#c inc -20 if c == 10
#These instructions would be processed as follows:

#Because a starts at 0, it is not greater than 1, and so b is not modified.
#a is increased by 1 (to 1) because b is less than 5 (it is 0).
#c is decreased by -10 (to 10) because a is now greater than or equal to 1 (it is 1).
#c is increased by -20 (to -10) because c is equal to 10.
#After this process, the largest value in any register is 1.

#You might also encounter <= (less than or equal to) or != (not equal to). However, the CPU doesn't have the bandwidth to tell you what all the registers are named, and leaves that to you to determine.

#What is the largest value in any register after completing the instructions in your puzzle input?

#--- Part Two ---

#To be safe, the CPU also needs to know the highest value held in any register during this process so that it can decide how much memory to allocate to these operations. 
#For example, in the above instructions, the highest value ever held was 10 (in register c after the third instruction was evaluated).

from FileReader import read_file

#=============================================================================
def reg_for_letter(letter, registries):
#
# Take a text line that looks like 
# qen inc 774 if ntk == 4
# and make a proper list with it
#
#-----------------------------------------------------------------------------
    for i in range(0, len(registries)):
        if (registries[i][0] == letter):
            return i

    registries.append([letter, 0])
    return len(registries) -1


#=============================================================================
def run_day_8():
#
#-----------------------------------------------------------------------------
    file = read_file("Day8_Data.txt")
    instructions = []
    registries = []
    for line in file:
        instructions.append(line.split(" "))

    running_max = -1000
    for feed in instructions:
        for value in registries:
            if (value[1] > running_max):
                running_max = value[1]
        change_reg = reg_for_letter(feed[0], registries)
        plus_minus = 1
        if (feed[1] == "dec"):
            plus_minus = -1
        change_diff = int(feed[2]) * plus_minus
        check_reg = reg_for_letter(feed[4], registries)
        check_condition = feed[5]
        check_num = int(feed[6])
        edit_reg = True
        if (check_condition == "=="):
            edit_reg = (registries[check_reg][1] == check_num)
        elif (check_condition == "!="):
            edit_reg = (registries[check_reg][1] != check_num)
        elif (check_condition == "<"):
            edit_reg = (registries[check_reg][1] < check_num)
        elif (check_condition == "<="):
            edit_reg = (registries[check_reg][1] <= check_num)
        elif (check_condition == ">"):
            edit_reg = (registries[check_reg][1] > check_num)
        elif (check_condition == ">="):
            edit_reg = (registries[check_reg][1] >= check_num)
        else :
            print("Unexpeced condition " + check_condition)
            exit()
        if (edit_reg):
            registries[change_reg][1] += change_diff
    print (registries)
    max_current = -1000
    for value in registries:
        if (value[1] > max_current):
            max_current = value[1]
    return running_max