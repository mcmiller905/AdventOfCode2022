def runPart1():
    inputFile = open('InputFiles/day1Input.txt', 'r')
    numbers = inputFile.readlines()
    elfTotal = 0
    biggestElf = 0
    index = 0
    while(True):
        if(index >= len(numbers)):
            break
        currentLine = numbers[index]
        if(currentLine == "\n"):
            if(elfTotal > biggestElf):
                biggestElf = elfTotal
            elfTotal = 0
        else:
            elfTotal = elfTotal + int(currentLine)
        index+=1
    return(biggestElf)

def runPart2():
    inputFile = open('InputFiles/day1Input.txt', 'r')
    numbers = inputFile.readlines()
    elfTotal = 0
    elfArray = []
    index = 0
    while(True):
        if(index >= len(numbers)):
            break
        currentLine = numbers[index]
        if(currentLine == "\n"):
            elfArray.append(elfTotal)
            elfTotal = 0
        else:
            elfTotal = elfTotal + int(currentLine)
        index+=1
    elfArray.sort(reverse=True)
    top3Total = elfArray[0] + elfArray[1] + elfArray[2]
    return(top3Total)