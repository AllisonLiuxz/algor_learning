def defineMove():
    move = list()
    move.append([0, -1])
    move.append([1, 0])
    move.append([-1, 0])
    move.append([0, 1])
    return move

def printMaze(maze, i, j):
    mazeTemp = maze
    mazeTemp[i][j] = '*'
    for count in range(len(mazeTemp)):
        print mazeTemp[count]
    raw_input()

def is_solevable(maze, n, m):

    #add wall to maze
    col = len(maze)
    row = len(maze[0])
    for count in range(col):
        maze[count].insert(0, 1)
        maze[count].append(1)

    maze = map(list, zip(*maze))


    for count in range(0, row+2):
        maze[count].insert(0, 1)
        maze[count].append(1)
    maze = map(list, zip(*maze))

    move = defineMove()
    mazeStack = list()
    temp = [1, 1, -1]
    mazeStack.append(temp)
    while mazeStack != []:
        temp = mazeStack.pop()
        x = temp[0]
        y = temp[1]
        d = temp[2] + 1
        while d < 4:
            i = x + move[d][0]
            j = y + move[d][1]
            if maze[i][j] == 0:
                printMaze(maze, i, j)
                temp = [x, y, d]
                mazeStack.append(temp)
                x = i
                y = j
                maze[x][y] = -1
                if (x == n and y == m):
                    return True
                else:
                    d = 0
            else:
                d += 1
    return False

mess = [[0,1,1,1,1],[0,0,1,1,1], [1,0,1,1,1],[1,1,1,1,0]]

print is_solevable(mess, 4, 4)