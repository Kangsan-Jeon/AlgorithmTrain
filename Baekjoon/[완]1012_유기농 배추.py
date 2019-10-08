dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]


def solve(arr, candidate, m, n):
    cnt = 0
    bfs = []
    while (len(candidate) != 0):
        if len(bfs) == 0:
            bfs.append(candidate[0])
            cnt += 1

        x, y = bfs.pop(0)
        if arr[y][x] == 2:
            continue
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if (0 <= next_x and next_x < m and 0 <= next_y and next_y < n):
                if arr[next_y][next_x] == 1:
                    bfs.append((next_x, next_y))
        candidate.remove((x, y))
        arr[y][x] = 2
    return cnt


def main():
    T = int(input())
    for t in range(T):
        M, N, K = (int(i) for i in input().split())
        arr = [[0 for _ in range(M)] for _ in range(N)]
        baechu = []
        for i in range(K):
            x, y = (int(x) for x in input().split())
            arr[y][x] = 1
            baechu.append((x, y))
        print(solve(arr, baechu, M, N))

if __name__ == "__main__":
    main()
