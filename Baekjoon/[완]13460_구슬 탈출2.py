from collections import deque

'''
Algorithm : BFS
1. 구슬은 빨간 구슬과 파란 구슬이 둘 중 하나라도 움직일 수 있는 방향으로 움직인다.
2. 움직임은 move함수로 구현되며 다 움직인 결과 좌표가 visited에 없는 경우 q에 추가한다.
=> q에 추가한다면 파란 구슬의 좌표와 빨간 구슬의 좌표 모두 visited에 함께 저장한다.
※ 한 턴에 둘 중 하나라도 움직인다면 전혀 다른 상황이므로 빨간 구슬과 파란 구슬의 좌표는 visited에 함께 저장해야한다.
3. 빨간 구슬만 홀에 들어갈 경우 move함수는 횟수를 반환한다.
=> 파란 구슬이 홀에 들어가거나 홀에 들어간 구슬이 없는 경우 0을 반환한다.
'''

dx = [-1, 1, 0, 0]  # left, right, up, down
dy = [0, 0, -1, 1]

def move(myMap, visited, blue, red, d_y, d_x, cnt, myQ):
    red_y, red_x = red
    blue_y, blue_x = blue
    red_state = False
    blue_state = False

    # 파랑 구슬과 빨간 구슬 중 하나가 벽에 부딪힐 때까지 go
    while(myMap[red_y][red_x] != "#" and myMap[blue_y][blue_x] != "#"):
        if myMap[red_y][red_x] == "O":
            red_state = True
            break
        if myMap[blue_y][blue_x] == "O":
            blue_state = True
            break
        red_y += d_y
        red_x += d_x
        blue_y += d_y
        blue_x += d_x

    # 파란구슬이 홀에 들어가면 return 0
    if blue_state:
        return 0

    # 빨간 구슬이 벽에 부딪히거나 홀에 들어갔을 때, 파란 구슬을 마저 움직임
    if myMap[red_y][red_x] == "#" or red_state:
        while(myMap[blue_y][blue_x] != "#"):
            if myMap[blue_y][blue_x] == "O":
                blue_state = True
                break
            blue_y += d_y
            blue_x += d_x

            # 파란 구슬의 다음 경로가 빨간 구슬의 위치이고 빨간 구슬이 홀에 들어가지 않았을 때,
            # 파란 구슬은 더이상 움직이지 않는다
            if (blue_y, blue_x) == (red_y, red_x) and not red_state:
                blue_y -= d_y
                blue_x -= d_x
                break
    # 파란 구슬이 벽에 부딕히거나 홀에 들어갔을 때, 빨간 구슬을 마저 움직임
    else:
        while(myMap[red_y][red_x] != "#"):
            if myMap[red_y][red_x] == "O":
                red_state = True
                break
            red_y += d_y
            red_x += d_x
            # 빨간 구슬의 다음 경로가 파란 구슬의 위치이고 파란 구슬이 홀에 들어가지 않았을 때,
            # 빨간 구슬은 더이상 움직이지 않는다
            if (blue_y, blue_x) == (red_y, red_x) and not blue_state:
                red_y -= d_y
                red_x -= d_x
                break

    # 파란 구슬이 홀에 들어간 경우
    if blue_state:
        return 0
    # 빨간 구슬만 홀에 들어간 경우
    elif red_state:
        return cnt+1
    else:
        # 두 구슬 다 홀에 들어가지 않은 경우, 큐와 visited에 두 구슬의 위치를 추가
        temp = [(blue_y - d_y, blue_x - d_x), (red_y - d_y, red_x - d_x)]
        if (temp[0], temp[1]) not in visited:
            visited.append((temp[0], temp[1]))
            temp += [cnt+1]
            myQ.append(temp)
        return 0

def solve(myMap, blue, red):
    myQ = deque()
    myQ.append([blue, red, 0])
    visited = [(blue, red)]
    while (len(myQ) != 0):
        temp = myQ.popleft()
        blue_y, blue_x = temp[0]
        red_y, red_x = temp[1]
        cnt = temp[2]
        for i in range(4):
            new_red_y = red_y + dy[i]
            new_red_x = red_x + dx[i]
            new_blue_y = blue_y + dy[i]
            new_blue_x = blue_x + dx[i]
            if (myMap[new_red_y][new_red_x] != "#" or myMap[new_blue_y][new_blue_x] != "#"):
                flag = move(myMap, visited, (blue_y, blue_x), (red_y, red_x), dy[i], dx[i], cnt, myQ)
                if flag:
                    if flag > 10:
                        flag = -1
                    return flag
                else:
                    continue

    if len(myQ) == 0:
        return -1

def main():
    N, M = (int(x) for x in input().split())
    myMap = []
    for i in range(N):
        temp = list(input())
        for j in range(M):
            if temp[j] == "B":
                blue = (i, j)
            elif temp[j] == "R":
                red = (i, j)

        myMap.append(temp)

    result = solve(myMap, blue, red)
    print(result)


if __name__ == "__main__":
    main()