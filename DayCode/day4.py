def runPart1():
    inputFile = open('InputFiles/day4Input.txt', 'r')
    sectionList = inputFile.readlines()
    numOfUselessElves = 0
    for pair in sectionList:
        sections = pair.split(",") #["1-2","3-4"]
        elf1 = sections[0].split("-") #["1","2"]
        elf2 = sections[1].split("-") #["3","4"]
        # check if the start&end of elf1 are both inside the start/end of elf2, and reverse
        if((int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])) or (int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]))):
            numOfUselessElves += 1
    return(numOfUselessElves)

def runPart2():
    inputFile = open('InputFiles/day4Input.txt', 'r')
    sectionList = inputFile.readlines()
    numOfOverlaps = 0
    for pair in sectionList:
        sections = pair.split(",") #["1-2","3-4"]
        elf1 = sections[0].split("-") #["1","2"]
        elf2 = sections[1].split("-") #["3","4"]
        # check if either the start or end of elf1 is within the range of elf2
        if((int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1])) or (int(elf1[1]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1]))):
            numOfOverlaps += 1
    return(numOfOverlaps)