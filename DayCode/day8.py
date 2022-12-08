def runPart1():
    inputFile = open('InputFiles/day8Input.txt', 'r')
    forest = inputFile.readlines()
    rowIndex = 1
    numVisible = 0
    #add edges
    numVisible = 2 * (len(forest[0])-1)
    numVisible += (2 * len(forest)) - 4
    #check inners
    while rowIndex < len(forest)-1:
        row = forest[rowIndex].rstrip()
        colIndex = 1
        while colIndex < len(row)-1:
            currValue = row[colIndex]
            #check up
            innerRowIndex = rowIndex-1
            upVisible = True
            while innerRowIndex >= 0:
                if(int(forest[innerRowIndex][colIndex]) >= int(currValue)):
                    upVisible = False
                    break
                innerRowIndex -= 1
            #check down
            innerRowIndex = rowIndex+1
            downVisible = True
            while innerRowIndex < len(forest):
                if(int(forest[innerRowIndex][colIndex]) >= int(currValue)):
                    downVisible = False
                    break
                innerRowIndex += 1
            #check left
            innerColIndex = colIndex-1
            leftVisible = True
            while innerColIndex >= 0:
                if(int(forest[rowIndex][innerColIndex]) >= int(currValue)):
                    leftVisible = False
                    break
                innerColIndex -= 1
            #check right
            innerColIndex = colIndex+1
            rightVisible = True
            while innerColIndex < len(row):
                if(int(forest[rowIndex][innerColIndex]) >= int(currValue)):
                    rightVisible = False
                    break
                innerColIndex += 1
            if(upVisible or downVisible or leftVisible or rightVisible):
                numVisible += 1
            colIndex += 1
        rowIndex += 1
        
    return(numVisible)

def runPart2():
    inputFile = open('InputFiles/day8Input.txt', 'r')
    forest = inputFile.readlines()
    rowIndex = 1
    #check inners
    topViewDistance = 0
    while rowIndex < len(forest)-1:
        row = forest[rowIndex].rstrip()
        colIndex = 1
        while colIndex < len(row)-1:
            currValue = row[colIndex]
            #check up
            innerRowIndex = rowIndex-1
            upViewDistance = 0
            while innerRowIndex >= 0:
                upViewDistance += 1
                if(int(forest[innerRowIndex][colIndex]) >= int(currValue)):
                    break
                innerRowIndex -= 1
            #check down
            innerRowIndex = rowIndex+1
            downViewDistance = 0
            while innerRowIndex < len(forest):
                downViewDistance += 1
                if(int(forest[innerRowIndex][colIndex]) >= int(currValue)):
                    break
                innerRowIndex += 1
            #check left
            innerColIndex = colIndex-1
            leftViewDistance = 0
            while innerColIndex >= 0:
                leftViewDistance += 1
                if(int(forest[rowIndex][innerColIndex]) >= int(currValue)):
                    break
                innerColIndex -= 1
            #check right
            innerColIndex = colIndex+1
            rightViewDistance = 0
            while innerColIndex < len(row):
                rightViewDistance += 1
                if(int(forest[rowIndex][innerColIndex]) >= int(currValue)):
                    break
                innerColIndex += 1
            totalViewDistance = upViewDistance * downViewDistance * leftViewDistance * rightViewDistance
            if(totalViewDistance > topViewDistance):
                topViewDistance = totalViewDistance
            colIndex += 1
        rowIndex += 1
        
    return(topViewDistance)