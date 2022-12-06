def runPart1():
    inputFile = open('InputFiles/day6Input.txt', 'r')
    comStr = inputFile.readlines()[0]
    index = 4
    packetPos = 0
    while index < len(comStr):
        subStr = comStr[index-4:index]
        if(len(set(subStr)) == len(subStr)):
            packetPos = index
            break
        index+=1
    return(packetPos)

def runPart2():
    inputFile = open('InputFiles/day6Input.txt', 'r')
    comStr = inputFile.readlines()[0]
    index = 14
    messagePos = 0
    while index < len(comStr):
        subStr = comStr[index-14:index]
        if(len(set(subStr)) == len(subStr)):
            messagePos = index
            break
        index+=1
    return(messagePos)