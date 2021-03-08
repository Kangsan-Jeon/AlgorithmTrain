from sys import stdin
from collections import deque


def bfs(path, graph, visited, queue, K):
    results = []
    while(sum(visited) != len(path) and len(queue) > 0):
        node = queue.popleft()
        if graph[node] > K:
            break
        neighbor = path[node]
        for x in neighbor:
            if not visited[x]:
                queue.append(x)
                visited[x] = True
                graph[x] = graph[node] + 1
                if graph[x] == K:
                    results.append(x)
    return results


def main():
    N, M, K, X = map(int, stdin.readline().rstrip().split())
    path = [[] for _ in range(N)]
    for _ in range(M):
        start, end = (int(x) for x  in stdin.readline().rstrip().split())
        path[start-1].append(end-1)      
        
    queue = deque([X-1])

    graph = [-1]*N
    visited = [False]*N
    visited[X-1] = True
    graph[X-1] = 0
    result = bfs(path, graph,  visited, queue, K)
    result.sort()

    if len(result) == 0:
        print(-1)
    else:
        for x in result:
            print(x+1)

if __name__ == "__main__":
    main()