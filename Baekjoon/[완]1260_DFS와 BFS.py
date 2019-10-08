def dfs(arr, start):
    n = len(arr)
    visited = [0 for i in range(n)]
    stack = [start]
    result = []
    while (len(stack) != 0):
        temp = stack.pop()

        if visited[temp] != -1:
            visited[temp] = -1
            result.append(temp + 1)
        else:
            continue

        next_nodes = arr[temp]
        for i in range(len(next_nodes) - 1, -1, -1):
            if next_nodes[i] == 1:
                stack.append(i)

    return result


def bfs(arr, start):
    n = len(arr)
    que = [start]
    visited = [0 for i in range(n)]
    result = []
    while (len(que) != 0):
        temp = que.pop(0)

        if visited[temp] != -1:
            visited[temp] = -1
            result.append(temp + 1)
        else:
            continue

        next_nodes = arr[temp]
        for i in range(len(next_nodes)):
            if next_nodes[i] == 1:
                que.append(i)

    return result


if __name__ == "__main__":
    N, M, start = (int(i) for i in input().split())
    arr = [[0 for i in range(N)] for j in range(N)]
    for m in range(M):
        v1, v2 = (int(i) for i in input().split())
        arr[v1 - 1][v2 - 1] = 1
        arr[v2 - 1][v1 - 1] = 1

    print(*dfs(arr, start - 1))
    print(*bfs(arr, start - 1))