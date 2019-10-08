import queue

upperCase = [1, 2, 5, 6]
rightCase = [1, 3, 6, 7]
leftCase = [1, 3, 4, 5]
downCase = [1, 2, 4, 7]

def getUpper(graph, position, y, x):
    next_y = y - 1
    next_x = x
    result = []
    if next_y >= 0:
        if position[next_y][next_x] == 0 and graph[next_y][next_x] in upperCase:
            result.append((next_y, next_x))
    return result

def getDown(graph, position,y, x):
    row = len(graph)
    result = []
    next_y = y + 1
    next_x = x
    if next_y < row:
        if position[next_y][next_x] == 0 and graph[next_y][next_x] in downCase:
            result.append((next_y, next_x))
    return result

def getRight(graph, position,y, x):
    col = len(graph[0])
    result = []
    next_y = y
    next_x = x + 1
    if next_x < col:
        if position[next_y][next_x] == 0 and graph[next_y][next_x] in rightCase:
            result.append((next_y, next_x))
    return result

def getLeft(graph, position,y, x):
    result = []
    next_y = y
    next_x = x - 1
    if next_x >= 0:
        if position[next_y][next_x] == 0 and graph[next_y][next_x] in leftCase:
            result.append((next_y, next_x))
    return result

def getNext(graph, position, y, x):
    case = graph[y][x]
    result = []
    if case == 1:
        result += getUpper(graph, position, y, x)
        result += getDown(graph, position, y, x)
        result += getRight(graph, position, y, x)
        result += getLeft(graph, position, y, x)
    elif case == 2:
        result += getUpper(graph, position, y, x)
        result += getDown(graph, position, y, x)
    elif case == 3:
        result += getRight(graph, position, y, x)
        result += getLeft(graph, position, y, x)
    elif case == 4:
        result += getUpper(graph, position, y, x)
        result += getRight(graph, position, y, x)
    elif case == 5:
        result += getDown(graph, position, y, x)
        result += getRight(graph, position, y, x)
    elif case == 6:
        result += getDown(graph, position, y, x)
        result += getLeft(graph, position, y, x)
    else:
        result += getUpper(graph, position, y, x)
        result += getLeft(graph, position, y, x)
    return result

def getNum(position):
    cnt = 0
    for i in range(len(position)):
        for j in range(len(position[0])):
            if position[i][j] >= 1:
                cnt += 1
    return cnt

def solve(graph, position, myQ, t):
    if t == 1:
        return 1
    while (not myQ.empty()):
        y, x = myQ.get()
        nextPos = getNext(graph, position, y, x)
        for next_y, next_x in nextPos:
            if position[y][x] + 1 < t:
                myQ.put((next_y, next_x))
                position[next_y][next_x] = position[y][x] + 1
            elif position[y][x] + 1 == t:
                position[next_y][next_x] = position[y][x] + 1
    return getNum(position)

def main():
    T = int(input())
    for t in range(T):
        Y, X, hole_y, hole_x, L = (int(x) for x in input().split())
        graph = []
        position = [[0 for _ in range(X)] for _ in range(Y)]
        for i in range(Y):
            temp = [int(x) for x in input().split()]
            graph.append(temp)
        myQ = queue.Queue()
        myQ.put((hole_y, hole_x))
        position[hole_y][hole_x] = 1
        print("#{} {}".format(t+1, solve(graph, position, myQ, L)))

if __name__ == "__main__":
    main()