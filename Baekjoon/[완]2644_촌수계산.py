import sys

sys.setrecursionlimit(1500)

def dfs(graph, visited, myStack, Y, N):
    if len(myStack) == 0:
        return -1
    else:
        idx = myStack.pop()
        if idx == Y-1:
            return visited[idx]
        temp = graph[idx]
        for i in range(N):
            if temp[i] == 1 and visited[i] == -1:
                visited[i] = visited[idx] + 1
                myStack.append(i)
        return dfs(graph, visited, myStack, Y, N)


def main():
    N = int(input())
    X, Y = (int(x) for x in input().split())
    M = int(input())
    graph = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        temp_x, temp_y = (int(x) for x in input().split())
        graph[temp_y-1][temp_x-1] = 1
        graph[temp_x-1][temp_y-1] = 1
    myStack = [X-1]
    visited = [-1 for _ in range(N)]
    visited[X-1] = 0
    result = dfs(graph, visited, myStack, Y, N)
    print(result)

if __name__ == "__main__":
    main()