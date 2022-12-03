def runPart1():
    inputFile = open('InputFiles/day3Input.txt', 'r')
    packList = inputFile.readlines()
    total = 0
    for pack in packList:
        c1,c2 = pack[:len(pack)//2], pack[len(pack)//2:]
        for letter in c1:
            if(c2.__contains__(letter)):
                adj = 96
                if(letter.isupper()):
                    adj = 38
                total += ord(letter) - adj
                break
    return(total)

def runPart2():
    inputFile = open('InputFiles/day3Input.txt', 'r')
    packList = inputFile.readlines()
    total = 0
    index = 0
    while(index < len(packList)):
        p1,p2,p3 = packList[index],packList[index+1],packList[index+2]
        for letter in p1:
            if(p2.__contains__(letter) and p3.__contains__(letter)):
                adj = 96
                if(letter.isupper()):
                    adj = 38
                total += ord(letter) - adj
                break
        index += 3
    return(total)