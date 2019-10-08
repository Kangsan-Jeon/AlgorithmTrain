dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, myStack):
    M = len(graph)  # row
    N = len(graph[0])   # col
    area = 0
    while(len(myStack) != 0):
        y, x = myStack.pop()
        area += 1
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]
            if 0 <= n_x  and n_x < N and 0 <= n_y and n_y < M and graph[n_y][n_x] == 0:
                graph[n_y][n_x] = 2
                myStack.append((n_y, n_x))
    return area

def solve(graph):
    M = len(graph)  # row
    N = len(graph[0])   # col
    myStack = []
    myArea = []
    cnt = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 0:
                myStack.append((i, j))
                graph[i][j] = 2
                area = dfs(graph, myStack)
                cnt += 1
                myArea.append(area)
    myArea.sort()
    print(cnt)
    print(*myArea)

def main():
    M, N, K = (int(x) for x in input().split()) # M: row, N: column

    graph = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(K):
        x1, y1, x2, y2 = (int(x) for x in input().split())
        for x in range(x1, x2):
            for y in range(y1, y2):
                graph[y][x] = 1

    solve(graph)

if __name__ == "__main__":
    main()