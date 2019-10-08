class Cell:
    def __init__(self, time, lifespan, isNew, activated):
        self.lifespan = lifespan
        self.time = time
        self.isNew = isNew
        self.activated = activated

    def getTime(self):
        return self.time

    def getLifespan(self):
        return self.lifespan

    def getIsNew(self):
        return self.isNew

    def getActivated(self):
        return self.activated

    def setTime(self, time):
        self.time = time

    def setLifespan(self, lifespan):
        self.lifespan = lifespan

    def setIsNew(self, isNew):
        self.isNew = isNew

    def setActivated(self, activated):
        self.activated = activated

def breed(plate, k, willActivate, X, Y):
    if k == 0:
        return plate

    # make next plate
    if willActivate:
        nextPlate = []
        nextPlate.append([Cell(0, 0, False, False) for i in range(X[1]-X[0]+3)])
        for i in range(Y[0], Y[1]+1):
            nextPlate.append([Cell(0, 0, False, False)] + plate[i][X[0]:X[1]+1] + [Cell(0, 0, False, False)])
        nextPlate.append([Cell(0, 0, False, False) for i in range(X[1]-X[0]+3)])
        n = Y[1] - Y[0] + 3
        m = X[1] - X[0] + 3
        if X[0] == 0:
            X[0] += 1
            X[1] += 1
        if Y[0] == 0:
            Y[0] += 1
            Y[1] += 1
    else:
        nextPlate = []
        for i in range(Y[0], Y[1] + 1):
            nextPlate.append(plate[i][X[0]:X[1] + 1])
        n = Y[1] - Y[0] + 1
        m = X[1] - X[0] + 1
        if X[0] == 1:
            X[0] -= 1
            X[1] -= 1
        if Y[0] == 1:
            Y[0] -= 1
            Y[1] -= 1

    # position of newly added cell
    new_cell_pos = []

    willActivate = False

    for row in range(n):
        for col in range(m):
            curCell = nextPlate[row][col]
            curTime = curCell.getTime()
            curLifespan = curCell.getLifespan()
            curIsNew = curCell.getIsNew()
            curActivated = curCell.getActivated()

            # dead cell
            if curTime == -1:
                pass

            # void or active cell
            elif curTime == 0:
                # void cell
                if curLifespan == 0:
                    pass

                # activated cell -> death
                elif curActivated:
                    nextPlate[row][col].setTime(-1)

                # active cell
                else:

                    # upper
                    upperCell = nextPlate[row - 1][col]
                    upper_lifespan = upperCell.getLifespan()
                    upper_isNew = upperCell.getIsNew()
                    if upper_lifespan == 0 or upper_isNew == True:
                        if upper_lifespan < curLifespan:
                            nextPlate[row - 1][col] = Cell(curLifespan, curLifespan, True, False)
                        if (row - 1, col) not in new_cell_pos:
                            new_cell_pos.append((row - 1, col))

                    # under
                    underCell = nextPlate[row + 1][col]
                    under_lifespan = underCell.getLifespan()
                    under_isNew = underCell.getIsNew()
                    if under_lifespan == 0 or under_isNew == True:
                        if under_lifespan < curLifespan:
                            nextPlate[row + 1][col] = Cell(curLifespan, curLifespan, True, False)
                        if (row + 1, col) not in new_cell_pos:
                            new_cell_pos.append((row + 1, col))

                    # left
                    leftCell = nextPlate[row][col - 1]
                    left_lifespan = leftCell.getLifespan()
                    left_isNew = leftCell.getIsNew()
                    if left_lifespan == 0 or left_isNew == True:
                        if left_lifespan < curLifespan:
                            nextPlate[row][col - 1] = Cell(curLifespan, curLifespan, True, False)
                        if (row, col - 1) not in new_cell_pos:
                            new_cell_pos.append((row, col - 1))

                    # right
                    rightCell = nextPlate[row][col + 1]
                    right_lifespan = rightCell.getLifespan()
                    right_isNew = rightCell.getIsNew()
                    if right_lifespan == 0 or right_isNew == True:
                        if right_lifespan < curLifespan:
                            nextPlate[row][col + 1] = Cell(curLifespan, curLifespan, True, False)
                        if (row, col + 1) not in new_cell_pos:
                            new_cell_pos.append((row, col + 1))

                    nextPlate[row][col].setTime(curLifespan-1)
                    nextPlate[row][col].setActivated(True)

            # living and inactive cell
            else:
                if curTime == 1:
                    if curActivated:
                        pass
                    else:
                        willActivate = True

                if curIsNew == False:
                    nextPlate[row][col].setTime(curTime-1)

    if len(new_cell_pos) != 0:
        min_x = X[1]
        max_x = X[0]
        min_y = Y[1]
        max_y = Y[0]
        for r, c in new_cell_pos:
            nextPlate[r][c].setIsNew(False)
            if c < min_x:
                min_x = c
            elif c > max_x:
                max_x = c
            if r < min_y:
                min_y = r
            elif r > max_y:
                max_y = r
        X = [min(min_x, X[0]), max(max_x, X[1])]
        Y = [min(min_y, Y[0]), max(max_y, Y[1])]

    # for i in range(n):
    #     for j in range(m):
    #         print(nextPlate[i][j].getLifespan(), end=' ')
    #     print()
    # print(X, Y)
    # print()
    #
    # for i in range(n):
    #     for j in range(m):
    #         print(nextPlate[i][j].getTime(), end=' ')
    #     print()
    # print()


    return breed(nextPlate, k-1, willActivate, X, Y)

def countLivingCell(plate):

    row = len(plate)
    col = len(plate[0])
    cnt = 0

    for r in range(row):
        for c in range(col):
            curCell = plate[r][c]
            if curCell.getLifespan() > 0:
                if curCell.getTime() > 0 or (curCell.getTime() == 0 and not curCell.getActivated()):
                    cnt += 1
    return cnt

T = int(input())

for i in range(T):
    N, M, K = (int(j) for j in input().split())
    plate = []

    # make initial plate
    for row in range(N):
        line = [Cell(int(j), int(j), False, False) for j in input().split()]
        plate.append(line)

    result = breed(plate, K, False, [0, M-1], [0, N-1])
    print("#{} {}\n".format(i+1, countLivingCell(result)))