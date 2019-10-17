from collections import deque
import sys

'''
Algorithm
[BFS]
1. 최단 거리를 구하기 위해 BFS를 사용한다.
=> 가장 긴 경로는 myMap의 모든 좌표를 들린 후 도착점으로 가는 N*M이므로 minDist = N*M+1로 설정한다
2. 최단 거리는 solve 함수를 통해 minDist로 반환한다.
=> 이때 큐에는 현재 좌표의 위치와 지금까지의 거리 그리고 벽을 부순적이 있는지를 나타내는 flag를 함께 저장한다.
=> visited를 단순히 방문한 적이 있는지 없는지만 나타낼 경우 같은 좌표라도 벽을 뚫고 왔는지,
    그렇지 않고 왔는지가 다르므로 visited는 int변수를 저장한다.
    만약 벽을 뚫고 왔는데 이미 벽을 뚫고 온 경우가 있으면 이는 최소값이 될 수 없으므로 고려하지 않아도 된다.
    하지만 벽을 뚫지 않고 왔는데 벽을 뚫고 온 경우만 있을 경우 벽을 뚫지 않을 경우가 최소값이 될 수 있으므로 이를 고려해야 한다.
    (0 : 방문한 적 없음, 1 : 벽을 뚫고 도착, 2 : 벽을 뚫지 않고 도착, 3 : 두 가지 경우 모두 도착)
3. 큐가 비었지만 minDist가 처음 설정한 값과 같으면 도착지에 도달한 적이 없으므로 minDist = -1로 설정한다.

'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve(myMap, myQ, visited, N, M, minDist):
    while myQ:
        y, x, cnt, flag = myQ.popleft()
        if y == N-1 and x == M-1:
            minDist = min(minDist, cnt)
            continue
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if new_y >= 0 and new_y < N and new_x >= 0 and new_x < M:
                temp = myMap[new_y][new_x]
                temp_visited = visited[new_y][new_x]
                if temp == 0 and temp_visited != 3:
                    if flag:    # 벽을 뚫은 적이 있는 경우
                        if temp_visited == 0:
                            visited[new_y][new_x] = 1   # 벽을 뚫고 도착
                            myQ.append((new_y, new_x, cnt + 1, flag))
                        elif temp_visited == 2:
                            visited[new_y][new_x] = 3   # 벽을 뚫은 경우와 뚫지 않은 경우 모두 도착
                            myQ.append((new_y, new_x, cnt + 1, flag))
                    else:
                        if temp_visited == 0:
                            visited[new_y][new_x] = 2   # 벽을 뚫지 않고 도착
                            myQ.append((new_y, new_x, cnt + 1, flag))
                        elif temp_visited == 1:
                            visited[new_y][new_x] = 3   # 벽을 뚫은 경우와 뚫지 않은 경우 모두 도착
                            myQ.append((new_y, new_x, cnt + 1, flag))

                if temp == 1 and flag == False:
                    if temp_visited == 0:
                        visited[new_y][new_x] = 1
                        myQ.append((new_y, new_x, cnt+1, True))

    if minDist == N*M+1:    # 도착지에 도착한 경우가 없는 경우
        minDist = -1

    return minDist

def main():
    N, M = (int(x) for x in sys.stdin.readline().rstrip().split())
    myMap = []
    minDist = N*M+1
    for i in range(N):
        temp = list(sys.stdin.readline().rstrip())
        temp = [int(x) for x in temp]
        myMap.append(temp)
    myQ = deque()
    myQ.append((0, 0, 1, False))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 3
    result = solve(myMap, myQ, visited, N, M, minDist)
    print(result)

if __name__ == "__main__":
    main()