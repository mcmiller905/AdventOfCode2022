def runPart1():
    inputFile = open('InputFiles/day9Input.txt', 'r')
    stepList = inputFile.readlines()
    headX = 0
    headY = 0
    tailX = 0
    tailY = 0
    tailPosSet = {"0, 0"}
    for step in stepList:
        splitStep = step.split(" ")
        dir = splitStep[0]
        numSteps = int(splitStep[1])
        for i in range(numSteps):
            #move head according to instructions
            if(dir == "U"):
                headY += 1
            if(dir == "D"):
                headY -= 1
            if(dir == "L"):
                headX -= 1
            if(dir == "R"):
                headX += 1
            #move tail to adjust
            tailPosSet.add(str(tailX)+", "+str(tailY))
            if(not(abs(headX-tailX) <= 1 and abs(headY-tailY) <= 1)):
                #move vert if needed
                if(headY != tailY):
                    if(headY-tailY > 0):
                        tailY += 1
                    else:
                        tailY -= 1
                #move hor if needed
                if(headX != tailX):
                    if(headX-tailX > 0):
                        tailX += 1
                    else:
                        tailX -= 1
    tailPosSet.add(str(tailX)+", "+str(tailY))
    return(len(tailPosSet))

def runPart2():
    inputFile = open('InputFiles/day9Input.txt', 'r')
    stepList = inputFile.readlines()
    ropePoints = {
        "H": [0,0],
        "1": [0,0],
        "2": [0,0],
        "3": [0,0],
        "4": [0,0],
        "5": [0,0],
        "6": [0,0],
        "7": [0,0],
        "8": [0,0],
        "9": [0,0]
    }

    tailPosSet = {"0, 0"}
    for step in stepList:
        splitStep = step.split(" ")
        dir = splitStep[0]
        numSteps = int(splitStep[1])
        for i in range(numSteps):
            #move head according to instructions
            if(dir == "U"):
                ropePoints.get("H")[1] += 1
            if(dir == "D"):
                ropePoints.get("H")[1] -= 1
            if(dir == "L"):
                ropePoints.get("H")[0] -= 1
            if(dir == "R"):
                ropePoints.get("H")[0] += 1
            #move tail to adjust
            tailPosSet.add(str(ropePoints.get("9")[0])+", "+str(ropePoints.get("9")[1]))
            for x in range(9):
                currIndex = x+1
                currX = int(ropePoints.get(str(currIndex))[0])
                currY = int(ropePoints.get(str(currIndex))[1])
                prevIndex = x
                if(x==0):
                    prevIndex = "H"
                prevX = int(ropePoints.get(str(prevIndex))[0])
                prevY = int(ropePoints.get(str(prevIndex))[1])
                if(not(abs(prevX-currX) <= 1 and abs(prevY-currY) <= 1)):
                #move vert if needed
                    if(prevY != currY):
                        if(prevY-currY > 0):
                            currY += 1
                        else:
                            currY -= 1
                #move hor if needed
                    if(prevX != currX):
                        if(prevX-currX > 0):
                            currX += 1
                        else:
                            currX -= 1
                ropePoints.update({str(currIndex): [currX, currY]})
    tailPosSet.add(str(currX)+", "+str(currY))
    return(len(tailPosSet))