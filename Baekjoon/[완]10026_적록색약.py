import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def normal_dfs(myMap, visited, myStack, N):
    while (len(myStack) != 0):
        y, x = myStack.pop()
        color = myMap[y][x]
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
                if myMap[new_y][new_x] == color and visited[new_y][new_x] == False:
                    visited[new_y][new_x] = True
                    myStack.append((new_y, new_x))
    return 0

def colorWeakness_dfs(myMap, visited, myStack, N):
    while (len(myStack) != 0):
        y, x = myStack.pop()
        color = myMap[y][x]
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
                if color == "R" or color == "G":
                    if (myMap[new_y][new_x] == "R" or myMap[new_y][new_x] == "G") and visited[new_y][new_x] == False:
                        visited[new_y][new_x] = True
                        myStack.append((new_y, new_x))
                else:
                    if myMap[new_y][new_x] == color and visited[new_y][new_x] == False:
                        visited[new_y][new_x] = True
                        myStack.append((new_y, new_x))
    return 0

def solve(myMap, visited, N, colorWeakness):
    myStack = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                myStack.append((i, j))
                visited[i][j] = True
                if colorWeakness:
                    colorWeakness_dfs(myMap, visited, myStack, N)
                else:
                    normal_dfs(myMap, visited, myStack, N)
                cnt += 1
    return cnt

def main():
    N = int(sys.stdin.readline())
    myMap = []
    for i in range(N):
        temp = list(sys.stdin.readline().rstrip())
        myMap.append(temp)
    visited = [[False for _ in range(N)] for _ in range(N)]
    print(solve(myMap, visited, N, False), end= " ")
    visited = [[False for _ in range(N)] for _ in range(N)]
    print(solve(myMap, visited, N, True))


if __name__ == "__main__":
    main()