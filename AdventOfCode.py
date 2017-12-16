from Day1 import run_day_1
from Day2 import run_day_2
from Day3 import run_day_3
from Day4 import run_day_4
from Day5 import run_day_5
from Day6 import run_day_6
from Day7 import run_day_7
from Day8 import run_day_8
from Day9 import run_day_9
from Day10 import run_day_10
from Day11 import run_day_11
from Day12 import run_day_12
from Day13 import run_day_13
from Day14 import run_day_14
from Day15 import run_day_15
from Day16 import run_day_16

#=============================================================================
def choose_day():
#
#-----------------------------------------------------------------------------
    valid_days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    print ("Please pick a day to find the solution to options are:")
    print(valid_days)
    text = input()
    if (text == "1"):
        print("Okay getting day 1")
        return run_day_1()
    elif (text == "2"):
        print("Okay getting day 2")
        return run_day_2()
    elif (text == "3"):
        print("Okay getting day 3")
        return run_day_3()
    elif (text == "4"):
        print("Okay getting day 4")
        return run_day_4()
    elif (text == "5"):
        print("Okay getting day 5")
        return run_day_5()
    elif (text == "6"):
        print("Okay getting day 6")
        return run_day_6()
    elif (text == "7"):
        print("Okay getting day 7")
        return run_day_7()
    elif (text == "8"):
        print("Okay getting day 8")
        return run_day_8()
    elif (text == "9"):
        print("Okay getting day 9")
        return run_day_9()
    elif (text == "10"):
        print("Okay getting day 10")
        return run_day_10()
    elif (text == "11"):
        print("Okay getting day 11")
        return run_day_11()
    elif (text == "12"):
        print("Okay getting day 12")
        return run_day_12()
    elif (text == "13"):
        print("Okay getting day 13")
        return run_day_13()
    elif (text == "14"):
        print("Okay getting day 14")
        return run_day_14()
    elif (text == "15"):
        print("Okay getting day 15")
        return run_day_15()
    elif (text == "16"):
        print("Okay getting day 16")
        return run_day_16()
    else :
        print("Invalid day please pick again")
        return choose_day()


#=============================================================================
if __name__ == "__main__":
#
#-----------------------------------------------------------------------------
    print(choose_day())
