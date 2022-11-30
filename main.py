# Main runner of all the Advent of Code 2021 code. Change the 'day' variable to
# run the different day's code
from importlib import import_module

day = 1

print()
print("*--------------------")
print("*  DAY " + str(day))
print("*--------------------")
print()
module = import_module('DayCode.day'+str(day))
part1 = getattr(module, 'runPart1')
part1()
# part2 = getattr(module, 'runPart2')
# part2()