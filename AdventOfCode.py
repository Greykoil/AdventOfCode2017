from Day1 import run_day_1
from Day2 import run_day_2
from Day3 import run_day_3
from Day4 import run_day_4
from Day5 import run_day_5
from Day6 import run_day_6
from Day7 import run_day_7
from Day8 import run_day_8

#=============================================================================
def choose_day():
#
#-----------------------------------------------------------------------------
    valid_days = [1, 2, 3, 4, 5, 6, 7, 8]
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
    else :
        print("Invalid day please pick again")
        return choose_day()


#=============================================================================
if __name__ == "__main__":
#
#-----------------------------------------------------------------------------
    print(choose_day())
