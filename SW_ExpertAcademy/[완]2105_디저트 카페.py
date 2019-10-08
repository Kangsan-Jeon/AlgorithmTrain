import queue

# 0 : 좌상, 1 : 좌하, 2 : 우하, 3 : 우상
dx = [-1, -1, 1, 1]
dy = [-1, 1, 1, -1]

possibleDirection = [[0, 1, 3],
                     [0, 1, 2],
                     [1, 2, 3],
                     [0, 2, 3],
                     [0, 1, 2, 3]]

def go(graph, stack, start_x, start_y, dessert, pastDir, results):
    N = len(graph)
    if len(stack) == 0:
        return -1
    else:
        y, x, direction = stack.pop()
        for idx in possibleDirection[direction]:
            if idx not in pastDir:
                new_y = y + dy[idx]
                new_x = x + dx[idx]
                if 0 <= new_x and new_x < N and new_y >= 0 and new_y < N:
                    if new_x == start_x and new_y == start_y:
                        results.append(len(dessert))
                    else:
                        if graph[new_y][new_x] in dessert:
                            continue
                        else:
                            stack.append((new_y, new_x, idx))
                            if direction != idx:
                                go(graph, stack, start_x, start_y,
                                   dessert + [graph[new_y][new_x]],
                                   pastDir + [direction], results)
                            else:
                                go(graph, stack, start_x, start_y,
                                   dessert + [graph[new_y][new_x]],
                                   pastDir, results)

def solve(graph, N):
    myStack = []
    dessert = []
    pastDir = []
    results = []
    maxNum = -1
    for i in range(N):
        for j in range(N):
            dessert.clear()
            pastDir.clear()
            dessert.append(graph[i][j])
            results.clear()
            myStack.append((i, j, -1))
            go(graph, myStack, j, i, dessert, pastDir, results)
            # print("results = {}".format(results))
            if len(results) != 0:
                maxNum = max(maxNum, max(results))
    return maxNum

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        graph = []
        for i in range(N):
            temp = [int(x) for x in input().split()]
            graph.append(temp)
        result = solve(graph, N)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()