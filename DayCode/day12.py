class node:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist
 
    def __repr__(self):
        return f"node({self.row}, {self.col}, {self.dist})"


def minDistance(grid, source, destX, destY):

    # if not given, find the start and destination
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                source.row = row
                source.col = col
                grid[row] = grid[row].replace("S","a")
                #break
            if grid[row][col] == 'E':
                destX = row
                destY = col
                grid[row] = grid[row].replace("E", "z")
 
    # To maintain location visit status
    visited = [[False for _ in range(len(grid[0]))]
               for _ in range(len(grid))]
     
    queue = []
    queue.append(source)
    visited[source.row][source.col] = True

    # start looping through queue until destination is found
    while len(queue) != 0:
        source = queue.pop(0)

        # Destination found
        if (source.row == destX and source.col == destY):
            return source.dist
 
        # moving up
        if isValid(source.row - 1, source.col, grid, visited, grid[source.row][source.col]):
            queue.append(node(source.row - 1, source.col, source.dist + 1))
            visited[source.row - 1][source.col] = True
 
        # moving down
        if isValid(source.row + 1, source.col, grid, visited, grid[source.row][source.col]):
            queue.append(node(source.row + 1, source.col, source.dist + 1))
            visited[source.row + 1][source.col] = True
 
        # moving left
        if isValid(source.row, source.col - 1, grid, visited, grid[source.row][source.col]):
            queue.append(node(source.row, source.col - 1, source.dist + 1))
            visited[source.row][source.col - 1] = True
 
        # moving right
        if isValid(source.row, source.col + 1, grid, visited, grid[source.row][source.col]):
            queue.append(node(source.row, source.col + 1, source.dist + 1))
            visited[source.row][source.col + 1] = True
    
    return -1
 
# checking where move is valid or not
def isValid(x, y, grid, visited, currHeight):
    if ((x >= 0 and y >= 0)):
        if(x < len(grid) and y < len(grid[0])-1):
            # check the height difference to see if the move is possible
            if(ord(currHeight) - ord(grid[x][y]) >= -1) and (visited[x][y] == False):
                return True
    return False

def runPart1():
    inputFile = open('InputFiles/day12Input.txt', 'r')
    grid = inputFile.readlines()
    emptyNode = node(0,0,0)
    emptyDestX = 0
    emptyDestY = 0
    dist = minDistance(grid, emptyNode, emptyDestX, emptyDestY)
    return(dist)

def runPart2():
    inputFile = open('InputFiles/day12Input.txt', 'r')
    grid = inputFile.readlines()
    listOfAs = []
    minDist = -1
    destX = 0
    destY = 0

    # get all the As and handle the S and E
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                listOfAs.append(node(row,col,0))
                grid[row] = grid[row].replace("S","a")
            elif grid[row][col] == 'a':
                listOfAs.append(node(row,col,0))
            elif grid[row][col] == "E":
                destX = row
                destY = col
                grid[row] = grid[row].replace("E","z")
    
    # for each A, get the minDistance and save it if it is lower
    for a in listOfAs:
        dist = minDistance(grid, a, destX, destY)
        if(dist > -1):
            if(minDist == -1):
                minDist = dist
            elif(dist < minDist):
                minDist = dist

    return(minDist)