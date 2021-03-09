from sys import stdin
from collections import deque

dx = [-1 ,1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, dict_que, virus, N, S):
    t = 0
    while(t < S):
        for v in virus:
            if len(dict_que[v]) == 0:
                continue
            else:
                new_que = deque()
                while(len(dict_que[v]) > 0):
                    x, y = dict_que[v].popleft()
                    for i in range(4):
                        if (0 <= x + dx[i] < N) and (0 <= y + dy[i] < N):
                            next_x = x + dx[i]
                            next_y = y + dy[i]
                            if graph[next_x][next_y] == 0:
                                new_que.append((next_x, next_y))
                                graph[next_x][next_y] = v
                dict_que[v] = new_que
        t+=1
    return graph

def main():
    N, K = map(int, stdin.readline().rstrip().split())
    existed = [False]*K
    virus = []
    graph = []
    dict_que = dict()
    for i in range(N):
        line = stdin.readline().rstrip().split()
        for j in range(N):
            line[j] = int(line[j])
            if line[j] != 0:
                if not existed[line[j]-1]:
                    dict_que[line[j]] = deque([(i, j)])
                    existed[line[j]-1] = True
                    virus.append(line[j])
                else:
                    dict_que[line[j]].append((i, j))
        graph.append(line)
    
    S, X, Y = map(int, stdin.readline().rstrip().split())

    virus.sort()
    result = bfs(graph, dict_que, virus, N, S)
    print(result[X-1][Y-1])

if __name__ == "__main__":
    main()