# Main runner of all the Advent of Code 2021 code. Change the 'day' variable to
# run the different day's code, or set to 0 to run all
from importlib import import_module

day = 2
runPart1 = True
runPart2 = True

def runDay(dayNum):
    print()
    print("*--------------------")
    print("*  DAY " + str(dayNum))
    print("*--------------------")
    print()
    module = import_module('DayCode.day'+str(dayNum))
    if(runPart1):
        part1 = getattr(module, 'runPart1')
        print("Part 1:")
        part1()
    if(runPart2):
        part2 = getattr(module, 'runPart2')
        print("Part 2:")
        part2()

if(day == 0):
    i = 1
    while(i < 26):
        runDay(i)
        i+=1
else:
    runDay(day)

