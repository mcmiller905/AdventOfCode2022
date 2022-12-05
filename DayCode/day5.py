def runPart1():
    inputFile = open('InputFiles/day5Input.txt', 'r')
    instList = inputFile.readlines()
    stacks = {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": []
    }

    #parse starting pos
    index = 7
    while index >=0:
        line = instList[index]
        if(line[1] != " "):
            stacks["1"] += [line[1]]
        if(line[5] != " "):
            stacks["2"] += [line[5]]
        if(line[9] != " "):
            stacks["3"] += [line[9]]
        if(line[13] != " "):
            stacks["4"] += [line[13]]
        if(line[17] != " "):
            stacks["5"] += [line[17]]
        if(line[21] != " "):
            stacks["6"] += [line[21]]
        if(line[25] != " "):
            stacks["7"] += [line[25]]
        if(line[29] != " "):
            stacks["8"] += [line[29]]
        if(line[33] != " "):
            stacks["9"] += [line[33]]
        index-=1

    instList = instList[10:]
    for inst in instList:
        splitInst = inst.split(" ")
        num, origin, dest = splitInst[1], splitInst[3], splitInst[5].strip()
        for x in range(int(num)):
            stacks[dest] += stacks[origin].pop()
    retval = ""
    for y in range(9):
        retval += stacks[str(y+1)].pop()
    return(retval)

def runPart2():
    inputFile = open('InputFiles/day5Input.txt', 'r')
    instList = inputFile.readlines()
    stacks = {
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": []
    }

    #parse starting pos
    index = 7
    while index >=0:
        line = instList[index]
        if(line[1] != " "):
            stacks["1"] += [line[1]]
        if(line[5] != " "):
            stacks["2"] += [line[5]]
        if(line[9] != " "):
            stacks["3"] += [line[9]]
        if(line[13] != " "):
            stacks["4"] += [line[13]]
        if(line[17] != " "):
            stacks["5"] += [line[17]]
        if(line[21] != " "):
            stacks["6"] += [line[21]]
        if(line[25] != " "):
            stacks["7"] += [line[25]]
        if(line[29] != " "):
            stacks["8"] += [line[29]]
        if(line[33] != " "):
            stacks["9"] += [line[33]]
        index-=1

    instList = instList[10:]
    for inst in instList:
        splitInst = inst.split(" ")
        num, origin, dest = splitInst[1], splitInst[3], splitInst[5].strip()
        subStack = []
        for x in range(int(num)):
            subStack += stacks[origin].pop()
        for x in range(int(num)):
            stacks[dest] += subStack.pop()
    retval = ""
    for y in range(9):
        retval += stacks[str(y+1)].pop()
    return(retval)