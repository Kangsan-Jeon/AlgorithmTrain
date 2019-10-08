import queue
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve(graph, myQ):
    n = len(graph)
    result = 0
    table = [[1 for _ in range(n)] for _ in range(n)]

    while (not myQ.empty()):
        y, x = myQ.get()
        height = graph[y][x]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x and next_x < n and 0 <= next_y and next_y < n and height > graph[next_y][next_x]:
                table[next_y][next_x] = table[y][x] + 1
                result = table[y][x] + 1
                myQ.put((next_y, next_x))

    return result

def setMap(graph, K, maxList):
    copy = deepcopy(graph)
    result = 0
    n = len(graph)
    for i in range(n):
        for j in range(n):
            myQ = queue.Queue()
            for k in range(len(maxList)):
                myQ.put(maxList[k])
            copy[i][j] -= K
            result = max(solve(copy, myQ), result)
            copy[i][j] += K
    return result

def main():
    T = int(input())
    for t in range(T):
        N, K = (int(x) for x in input().split())
        maxList = []
        maxHeight = -5
        graph = []
        for i in range(N):
            temp = [int(x) for x in input().split()]
            for j in range(N):
                if maxHeight < temp[j]:
                    maxHeight = temp[j]
                    maxList.clear()
                    maxList.append((i, j))
                elif maxHeight == temp[j]:
                    maxList.append((i, j))
            graph.append(temp)

        result = 0
        while (K >= 0):
            result = max(result, setMap(graph, K, maxList))
            K-=1
        print("#{} {}".format(t+1, result))


if __name__ == "__main__":
    main()