def runPart1():
    inputFile = open('InputFiles/day11Input.txt', 'r')
    inputLines = inputFile.readlines()
    itemsMap = {}
    opMap = {} # "new = old * 2" becomes ["*", "2"]
    testMap = {}
    trueMap = {}
    falseMap = {}
    monkeyUse = [0,0,0,0,0,0,0,0]
    currMonkey = 0
    for line in inputLines:
        line = line.strip()
        if line.startswith("Monkey"):
            currMonkey = line.split(" ")[1][:1]
        elif line.startswith("Starting"):
            itemsStr = line.split(": ")[1]
            itemArray = itemsStr.split(", ")
            itemsMap.update({currMonkey: itemArray})
        elif line.startswith("Operation"):
            opStr = line.split(": ")[1]
            opArray = opStr.split(" ")
            opMap.update({currMonkey: [opArray[3], opArray[4]]})
        elif line.startswith("Test"):
            testArray = line.split(" ")
            testMap.update({currMonkey: int(testArray[3])})
        elif line.startswith("If true"):
            trueMap.update({currMonkey: line.split(" ")[5]})
        elif line.startswith("If false"):
            falseMap.update({currMonkey: line.split(" ")[5]})
    
    #process through monkeys
    round = 1
    while round <= 20:
        for currMonkey in itemsMap.keys():
            for item in itemsMap.get(currMonkey):
                monkeyUse[int(currMonkey)] += 1
                newVal = 0
                #do starting operation
                if(opMap.get(currMonkey)[0] == "*"):
                    if(opMap.get(currMonkey)[1] == "old"):
                        newVal = int(item) * int(item)
                    else:
                        newVal = int(item) * int(opMap.get(currMonkey)[1])
                elif(opMap.get(currMonkey)[0] == "+"):
                    if(opMap.get(currMonkey)[1] == "old"):
                        newVal = int(item) + int(item)
                    else:
                        newVal = int(item) + int(opMap.get(currMonkey)[1])
                #get bored
                newVal = newVal // 3
                #do test
                recievingMonkey = falseMap.get(currMonkey)
                if(newVal % testMap.get(currMonkey) == 0):
                    recievingMonkey = trueMap.get(currMonkey)
                #toss
                newMonkList = []
                newMonkList = itemsMap.get(recievingMonkey)
                newMonkList.append(newVal)
                itemsMap.update({recievingMonkey: newMonkList})
            itemsMap.update({currMonkey: []})
        round += 1
    topMonkey = max(monkeyUse)
    monkeyUse.remove(topMonkey)
    secMonkey = max(monkeyUse)
    return(topMonkey * secMonkey)

def runPart2():
    inputFile = open('InputFiles/day11Input.txt', 'r')
    inputLines = inputFile.readlines()
    itemsMap = {}
    opMap = {} # "new = old * 2" becomes ["*", "2"]
    testMap = {}
    prodOfDiv = 1
    trueMap = {}
    falseMap = {}
    monkeyUse = [0,0,0,0,0,0,0,0]
    currMonkey = 0
    for line in inputLines:
        line = line.strip()
        if line.startswith("Monkey"):
            currMonkey = line.split(" ")[1][:1]
        elif line.startswith("Starting"):
            itemsStr = line.split(": ")[1]
            itemArray = itemsStr.split(", ")
            itemsMap.update({currMonkey: itemArray})
        elif line.startswith("Operation"):
            opStr = line.split(": ")[1]
            opArray = opStr.split(" ")
            opMap.update({currMonkey: [opArray[3], opArray[4]]})
        elif line.startswith("Test"):
            testArray = line.split(" ")
            testMap.update({currMonkey: int(testArray[3])})
            prodOfDiv *= int(testArray[3])
        elif line.startswith("If true"):
            trueMap.update({currMonkey: line.split(" ")[5]})
        elif line.startswith("If false"):
            falseMap.update({currMonkey: line.split(" ")[5]})
    
    #process through monkeys
    round = 1
    while round <= 10_000:
        for currMonkey in itemsMap.keys():
            for item in itemsMap.get(currMonkey):
                monkeyUse[int(currMonkey)] += 1
                newVal = 0
                #do starting operation
                if(opMap.get(currMonkey)[0] == "*"):
                    if(opMap.get(currMonkey)[1] == "old"):
                        newVal = int(item) * int(item)
                    else:
                        newVal = int(item) * int(opMap.get(currMonkey)[1])
                elif(opMap.get(currMonkey)[0] == "+"):
                    if(opMap.get(currMonkey)[1] == "old"):
                        newVal = int(item) + int(item)
                    else:
                        newVal = int(item) + int(opMap.get(currMonkey)[1])
                #get bored
                newVal = newVal % prodOfDiv
                #do test
                recievingMonkey = falseMap.get(currMonkey)
                if(newVal % testMap.get(currMonkey) == 0):
                    recievingMonkey = trueMap.get(currMonkey)
                #toss
                newMonkList = []
                newMonkList = itemsMap.get(recievingMonkey)
                newMonkList.append(newVal)
                itemsMap.update({recievingMonkey: newMonkList})
            itemsMap.update({currMonkey: []})
        round += 1
    topMonkey = max(monkeyUse)
    monkeyUse.remove(topMonkey)
    secMonkey = max(monkeyUse)
    return(topMonkey * secMonkey)