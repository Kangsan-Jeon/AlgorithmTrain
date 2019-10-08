dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def getMinDistance(arr, cnt):

    N = len(arr)
    M = len(arr[0])
    bfs = [(0, 0)]
    dist = []
    cnt[0][0] = 1

    while (len(bfs) != 0):
        x, y = bfs.pop(0)

        if x == M - 1 and y == N - 1:
            return cnt[y][x]

        if arr[y][x] == -1:
            continue
        else:
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N:
                    temp = arr[new_y][new_x]
                    if temp == 1:
                        bfs.append((new_x, new_y))
                        cnt[new_y][new_x] = 1 + cnt[y][x]

                    else:
                        continue
            arr[y][x] = -1


if __name__ == "__main__":
    N, M = (int(i) for i in input().split())
    arr = []
    for i in range(N):
        line = input()
        temp = []
        for j in range(M):
            temp.append(int(line[j]))
        arr.append(temp)

    cnt = [[0 for i in range(M)] for j in range(N)]

    result = getMinDistance(arr, cnt)
    print(result)

