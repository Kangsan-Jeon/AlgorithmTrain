import heapq

'''
Algotirhm
[BFS, Simulation]
목표 : K시간 이후 살아있는 줄기세포의 수를 반환
1. 최악의 경우 K의 최대값인 300시간 동안 매시간 행이나 열이 커질 수 있으므로 최대 배열의 크기는 650x650로 잡는다.
2. 새로 생길 줄기세포는 생명력 수치가 높은 것에 따라야 하므로 새로 생길 줄기세포임을 나타내는 isNew라는 배열을 선언한다.
3. 아직 활성화되지 않은 세포와 활성화된 세포는 cells라는 heap에 저장한다.
=> 우선순위는 활성화 되는 시간이나 세포가 죽는 시간이 작은 것이 높다.
=> cells에는 활성화 되는 시간 또는 세포가 죽는 시간과 줄시세포의 좌표 그리고 활성화 된 세포인지 나타내는 변수 isActive를 함께 저장한다.
=> isActive가 False일 때 t는 활성화 되는 시간이고 True일 때는 죽는 시간이다.
4. solve함수에서는 매초 wait에 있는 세포를 번식시키고 죽는 세포와 활성화 되는 세포를 처리한다.
=> 활성화 되면 1시간 뒤 줄기세포가 번식하므로 번식될 세포의 위치를 wait에 추가한 뒤 1시간 뒤에 처리한다.
=> wait에서 꺼낸 세포의 좌표에 대해서 isNew를 False로 갱신하고 heap에 추가한다.
=> 추가할 때 죽는 시간 t는 현재 시간 + 생명력 수치이고 isActive는 True이다.
5. 시간이 K가 되면 살아있는 세포는 cells에 모두 들어있으므로 cells의 크기를 반환한다.
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
plate = [[0 for _ in range(650)] for _ in range(650)]
isNew = [[False for _ in range(650)] for _ in range(650)]

def solve(plate, isNew, cells, K):
    time = 1
    wait = []
    while (time <= K):
        while wait:
            y, x = wait.pop()
            isNew[y][x] = False
            heapq.heappush(cells, (time + plate[y][x], y, x, False))

        while (cells[0][0] == time):
            t, y, x, isActive = (heapq.heappop(cells))
            if isActive:
                continue
            else:
                heapq.heappush(cells, (time + plate[y][x], y, x, True))
                k = plate[y][x]
                for i in range(4):
                    next_y = y + dy[i]
                    next_x = x + dx[i]
                    if next_y >= 0 and next_y < 650 and next_x >= 0 and next_x < 650 and \
                        (plate[next_y][next_x] == 0 or isNew[next_y][next_x] is True):
                            temp = plate[next_y][next_x]
                            if temp == 0:
                                wait.append((next_y, next_x))
                                plate[next_y][next_x] = k
                                isNew[next_y][next_x] = True

                            elif temp < k:
                                plate[next_y][next_x] = k
        time += 1
    return len(cells)

def main():
    T = int(input())
    for t in range(T):
        N, M, K = (int(x) for x in input().split())
        cells = []
        for i in range(650):
            for j in range(650):
                plate[i][j] = 0
        for i in range(N):
            temp = input().split()
            for j in range(len(temp)):
                temp[j] = int(temp[j])
                if temp[j] > 0:
                    heapq.heappush(cells, (temp[j], 300 + i, 300 + j, False))
                plate[300+i][300+j] = temp[j]
        result = solve(plate, isNew, cells, K)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()