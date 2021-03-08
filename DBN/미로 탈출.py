from sys import stdin
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(miro, cnts, que, N, M):
    while (len(que) > 0):
        y, x = que.popleft()
        if y == N-1 and x == M-1:
            break
        else:
            for i in range(4):
                if (0 <= y + dy[i] < N) and (0 <= x + dx[i] < M):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if miro[next_y][next_x] == 1 and cnts[next_y][next_x] == N*M+1:
                        que.append((next_y, next_x))
                        cnts[next_y][next_x] = cnts[y][x] + 1 
    print(cnts[N-1][M-1])


def main():
    N, M = map(int, stdin.readline().rstrip().split())
    cnts = [[N*M+1 for _ in range(M)] for _ in range(N)]

    miro = [list(map(int, list(stdin.readline().rstrip()))) for _ in range(N)]

    que = deque([(0, 0)])

    cnts[0][0] = 1
    bfs(miro, cnts, que, N, M)    

if __name__ == "__main__":
    main()