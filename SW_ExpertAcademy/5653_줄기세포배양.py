import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve(plate, cells, K):
    time = 1
    wait = []
    while (time <= K):
        print(time)
        print(cells)
        print(wait)
        while wait:
            y, x = wait.pop()
            plate[y][x][1] = False
            heapq.heappush(cells, (time + plate[y][x][0], y, x, False))

        while (cells[0][0] == time):
            t, y, x, isActive = heapq.heappop(cells)
            if isActive:
                continue
            else:
                heapq.heappush(cells, (time + plate[y][x][0], y, x, True))
                k = plate[y][x][0]
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if next_y >= 0 and next_y < 650 and next_x >= 0 and next_x < 650 \
                            and (plate[next_y][next_x][0] == 0 or plate[next_y][next_x][1] == True):
                        temp = plate[next_y][next_x][0]
                        if temp < k:
                            if temp == 0:
                                wait.append((next_y, next_x))
                                plate[next_y][next_x][1] = True
                            plate[next_y][next_x][0] = k
        time += 1
    return len(cells)

def main():
    T = int(input())
    for t in range(T):
        N, M, K = (int(x) for x in input().split())
        plate = [[[0, False] for _ in range(650)] for _ in range(650)]
        cells = []
        for i in range(N):
            temp = input().split()
            for j in range(len(temp)):
                temp[j] = int(temp[j])
                if temp[j] > 0:
                    heapq.heappush(cells, (temp[j], 300 + i, 300 + j, False))
                plate[300+i][300+j][0] = temp[j]
        result = solve(plate, cells, K)
        print("#{} {}".format(t+1, result))



if __name__ == "__main__":
    main()