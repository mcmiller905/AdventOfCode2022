def runPart1():
    inputFile = open('InputFiles/day7Input.txt', 'r')
    commands = inputFile.readlines()
    fileTree = {}
    index = 0
    currDir = ""
    # make the fileTree
    while index < len(commands):
        line = commands[index].strip()
        if line[0] == "$":
            command = line[2:].split(" ")
            # cd command
            if(command[0] == "cd"):
                if(command[1] == ".."):
                    splitDir = currDir.split("/")
                    currDir = '/'.join(splitDir[:len(splitDir)-2]) + "/"
                else:
                    currDir += command[1] + "/"
        else:
            splitLine = line.split(" ")
            if(splitLine[0].isnumeric()):
                #just get sizes
                splitDir = currDir.split("/")
                hierLoc = len(splitDir)
                while hierLoc > 1:
                    fileLoc = '/'.join(splitDir[:hierLoc-1]) + "/"
                    if(fileLoc == "/"):
                        break
                    if(fileLoc in fileTree):
                        oldVal = int(fileTree.get(fileLoc))
                        newVal = oldVal + int(splitLine[0])
                        fileTree.update({fileLoc: newVal})
                    else:
                        fileTree.update({fileLoc: int(splitLine[0])})
                    hierLoc -= 1
        index += 1
    #add up all dirs below 100_000    
    total = 0
    for key in fileTree:
        if(fileTree.get(key) <= 100_000):
            total += fileTree.get(key)
    return(total)

def runPart2():
    inputFile = open('InputFiles/day7Input.txt', 'r')
    commands = inputFile.readlines()
    fileTree = {}
    index = 0
    currDir = ""
    # make the fileTree
    while index < len(commands):
        line = commands[index].strip()
        if line[0] == "$":
            command = line[2:].split(" ")
            # cd command
            if(command[0] == "cd"):
                if(command[1] == ".."):
                    splitDir = currDir.split("/")
                    currDir = '/'.join(splitDir[:len(splitDir)-2]) + "/"
                else:
                    currDir += command[1] + "/"
        else:
            splitLine = line.split(" ")
            if(splitLine[0].isnumeric()):
                #just get sizes
                splitDir = currDir.split("/")
                hierLoc = len(splitDir)
                while hierLoc > 1:
                    fileLoc = '/'.join(splitDir[:hierLoc-1]) + "/"
                    if(fileLoc == "/"):
                        break
                    if(fileLoc in fileTree):
                        oldVal = int(fileTree.get(fileLoc))
                        newVal = oldVal + int(splitLine[0])
                        fileTree.update({fileLoc: newVal})
                    else:
                        fileTree.update({fileLoc: int(splitLine[0])})
                    hierLoc -= 1
        index += 1
    # find size needed to delete and get the smallest amount that works
    driveSize = 70_000_000
    neededSpace = 30_000_000
    freeSpace = driveSize - fileTree.get("//")
    amountToDelete = neededSpace - freeSpace
    deleteSize = 70_000_000
    for key in fileTree:
        if(fileTree.get(key) > amountToDelete):
            if(fileTree.get(key) < deleteSize):
                deleteSize = fileTree.get(key)
    return(deleteSize)