def runPart1():
    inputFile = open('InputFiles/day10Input.txt', 'r')
    cmdList = inputFile.readlines()
    cycleNum = 1
    cmdNum = 0
    moreCommands = True
    numToAdd = 0
    x = 1
    outputMap = {
        20: 0,
        60: 0,
        100: 0,
        140: 0,
        180: 0,
        220: 0
    }
    while(moreCommands):
        if(cycleNum in outputMap.keys()):
            outputMap.update({cycleNum: cycleNum*x})
        if(numToAdd != 0):
            x += numToAdd
            numToAdd = 0
            cmdNum += 1
        else:
            cmd = cmdList[cmdNum].rstrip()
            if(cmd == "noop"):
                cmdNum += 1
            elif(cmd.startswith("addx")):
                splitCmd = cmd.split(" ")
                numToAdd = int(splitCmd[1])
        cycleNum += 1
        if(cmdNum >= len(cmdList)):
            moreCommands = False
    return(sum(outputMap.values()))

def runPart2():
    inputFile = open('InputFiles/day10Input.txt', 'r')
    cmdList = inputFile.readlines()
    cycleNum = 1
    cmdNum = 0
    moreCommands = True
    numToAdd = 0
    x = 1
    outputStr = "#"
    while(moreCommands):
        if cycleNum % 40 == 0:
            outputStr += "\n"
        if(numToAdd != 0):
            x += numToAdd
            numToAdd = 0
            cmdNum += 1
        else:
            cmd = cmdList[cmdNum].rstrip()
            if(cmd == "noop"):
                cmdNum += 1
            elif(cmd.startswith("addx")):
                splitCmd = cmd.split(" ")
                numToAdd = int(splitCmd[1])
        if x-1 == (cycleNum%40) or x == (cycleNum%40) or x+1 == (cycleNum%40):
            outputStr += "#"
        else:
            outputStr += "."
        cycleNum += 1
        if(cmdNum >= len(cmdList)):
            moreCommands = False
    return(outputStr[:len(outputStr)-1])