from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve(arr, bfs, M, N, tot0_num):
    time = [[0 for i in range(M)] for j in range(N)]
    change = 0
    while (len(bfs) != 0):
        x, y = bfs.popleft()
        time0 = time[y][x]
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N:
                temp = arr[new_y][new_x]
                if temp == 2 or temp == -1:  # visited
                    continue
                else:
                    if temp == 0:
                        change += 1
                        if change == tot0_num:
                            return time0 + 1
                        time[new_y][new_x] = time0 + 1
                    arr[new_y][new_x] = 2
                    bfs.append((new_x, new_y))
    return -1

def main():
    M, N = (int(i) for i in input().split())
    tomato = []
    bfs = deque([])
    tot0_num = 0    # 안 익은 토마토 개수
    for i in range(N):
        temp = input().split()
        for j in range(M):
            x = temp[j]
            temp[j] = int(x)
            if x == '1':
                bfs.append((j, i))
            elif x == '0':
                tot0_num += 1
        tomato.append(temp)

    if tot0_num == 0:
        print(0)
    else:
        print(solve(tomato, bfs, M, N, tot0_num))

if __name__ == "__main__":
    main()