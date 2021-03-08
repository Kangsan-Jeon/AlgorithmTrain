from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, visited, stack, result, N, M):
    if len(stack) == 0:
        return result
    else:
        y, x = stack.pop()
        if not visited[y][x]:
            visited[y][x] = True
            is_continued = False
            for i in range(4):
                n_y = y + dy[i]
                n_x = x + dx[i]
                if (0 <= n_x < M) and (0 <= n_y < N):
                    if not visited[n_y][n_x]:
                        is_continued = True
                        stack.append((n_y, n_x))
            if not is_continued:
                result += 1
        return dfs(graph, visited, stack, result, N, M)
        
def main():
    N, M = map(int, stdin.readline().split())
    graph = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    stack = []
    result = 0

    for i in range(N):
        inp = stdin.readline().rstrip()
        row = []
        for j in range(M):
            if inp[j] == "0":
                stack.append((i, j))
                row.append(0)
            else:
                row.append(1)
                visited[i][j] = True
        graph.append(row)
    
    result = dfs(graph, visited, stack, result, N, M)
    print(result)

if __name__ == "__main__":
    main()