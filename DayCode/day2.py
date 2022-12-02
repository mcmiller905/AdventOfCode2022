def runPart1():
    inputFile = open('InputFiles/day2Input.txt', 'r')
    rounds = inputFile.readlines()
    score=0
    for round in rounds:
        theirs = round[0]
        mine = round[2]
        outcome = 0
        hand = 0
        if(theirs == "A"):
            if(mine == "X"):
                #tie
                outcome = 3
                hand = 1
            elif(mine == "Y"):
                #mine wins
                outcome = 6
                hand = 2
            else:
                #thiers wins
                outcome = 0
                hand = 3
        elif(theirs == "B"):
            if(mine == "X"):
                #they win
                outcome = 0
                hand = 1
            elif(mine == "Y"):
                #tie
                outcome = 3
                hand = 2
            else:
                #mine wins
                outcome = 6
                hand = 3
        else:
            if(mine == "X"):
                #mine wins
                outcome = 6
                hand = 1
            elif(mine == "Y"):
                #they wins
                outcome = 0
                hand = 2
            else:
                #tie
                outcome = 3
                hand = 3
        score += outcome + hand
    print(score)


def runPart2():
    inputFile = open('InputFiles/day2Input.txt', 'r')
    rounds = inputFile.readlines()
    score=0
    for round in rounds:
        theirs = round[0]
        neededOutcome = round[2]
        outcome = 0
        hand = 0
        if(theirs == "A"):
            if(neededOutcome == "X"):
                #lose, so Scissors
                outcome = 0
                hand = 3
            elif(neededOutcome == "Y"):
                #tie, so Rock
                outcome = 3
                hand = 1
            else:
                #win, so Paper
                outcome = 6
                hand = 2
        elif(theirs == "B"):
            if(neededOutcome == "X"):
                #lose, so Rock
                outcome = 0
                hand = 1
            elif(neededOutcome == "Y"):
                #tie, so Paper
                outcome = 3
                hand = 2
            else:
                #win, so Scissors
                outcome = 6
                hand = 3
        else:
            if(neededOutcome == "X"):
                #lose, so Paper
                outcome = 0
                hand = 2
            elif(neededOutcome == "Y"):
                #tie, so Scissors
                outcome = 3
                hand = 3
            else:
                #win, so Rock
                outcome = 6
                hand = 1
        score += outcome + hand
    print(score)