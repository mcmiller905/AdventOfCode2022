# Main runner of all the Advent of Code 2021 code. Change the 'day' variable to
# run the different day's code, or set to 0 to run all
from importlib import import_module
import time
import os

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
        startTime = time.perf_counter()
        answer = part1()
        endTime = time.perf_counter()
        print(f"Part 1: - {1000 * (endTime - startTime):0.4f}ms")
        print(str(answer))
    if(runPart2):
        part2 = getattr(module, 'runPart2')
        startTime = time.perf_counter()
        answer = part2()
        endTime = time.perf_counter()
        print(f"Part 2: - {1000 * (endTime - startTime):0.4f}ms")
        print(str(answer))

if(day == 0):
    numFiles = len(next(os.walk("DayCode"))[2]) + 1
    i = 1
    while(i < numFiles):
        runDay(i)
        i+=1
else:
    runDay(day)

