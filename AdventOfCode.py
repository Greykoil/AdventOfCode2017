from Day6 import run_day_6


#=============================================================================
def choose_day():
#
#-----------------------------------------------------------------------------
    valid_days = [6]
    print ("Please pick a day to find the solution to options are:")
    print(valid_days)
    text = input()
    if (text == "6"):
        print("Okay getting day 6")
        return run_day_6()
    else :
        print("Invalid day please pick again")
        return choose_day()


#=============================================================================
if __name__ == "__main__":
#
#-----------------------------------------------------------------------------
    print(choose_day())
