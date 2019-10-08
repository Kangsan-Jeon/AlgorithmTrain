dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(graph, visited, myStack, rain, N):
    while (len(myStack) != 0):
        y, x = myStack.pop()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
                if graph[new_y][new_x] > rain and (not visited[new_y][new_x]):
                    visited[new_y][new_x] = True
                    myStack.append((new_y, new_x))
    return 0

def getArea(graph, rain, N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    area = 0
    myStack = []
    for i in range(N):
        for j in range(N):
            if (not visited[i][j]) and graph[i][j] > rain:
                visited[i][j] = True
                myStack.append((i, j))
                DFS(graph, visited, myStack, rain, N)
                area += 1
    return area

def solve(graph, minHeight, maxHeight, N):
    maxArea = 0
    for i in range(minHeight, maxHeight):
        maxArea = max(maxArea, getArea(graph, i, N))
    return maxArea


def main():
    N = int(input())
    graph = []
    minHeight = 101
    maxHeight = 0
    for i in range(N):
        temp = []
        inp = input().split()
        for j in range(N):
            temp_num = int(inp[j])
            temp.append(temp_num)
            if temp_num > maxHeight:
                maxHeight = temp_num
            elif temp_num < minHeight:
                minHeight = temp_num
        graph.append(temp)

    if minHeight == maxHeight:
        result = 1
    else:
        result = solve(graph, minHeight, maxHeight, N)
    print(result)

if __name__ == "__main__":
    main()