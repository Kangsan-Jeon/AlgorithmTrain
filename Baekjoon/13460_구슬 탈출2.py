# 21:37

from collections import deque
from pprint import pprint

dx = [-1, 1, 0, 0]  # left, right, up, down
dy = [0, 0, -1, 1]

def go(myMap, table, visited, blue, red, d_y, d_x, myQ):
    # print("origin: red = {}, blue = {}".format(red, blue))
    red_y, red_x = red
    blue_y, blue_x = blue
    red_state = False
    blue_state = False
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
        table[red_y][red_x] = table[red[0]][red[1]] + 1

    if blue_state:
        return False

    if myMap[red_y][red_x] == "#" or red_state:
        while(myMap[blue_y][blue_x] != "#"):
            if myMap[blue_y][blue_x] == "O":
                blue_state = True
                break
            blue_y += d_y
            blue_x += d_x
            if (blue_y, blue_x) == (red_y, red_x) and not red_state:
                blue_y -= d_y
                blue_x -= d_x
                break
    else:
        while(myMap[red_y][red_x] != "#"):
            table[red_y][red_x] = table[red[0]][red[1]] + 1
            if myMap[red_y][red_x] == "O":
                red_state = True
                break
            red_y += d_y
            red_x += d_x
            if (blue_y, blue_x) == (red_y, red_x) and not blue_state:
                red_y -= d_y
                red_x -= d_x
                break

    if blue_state:
        return False
    elif red_state:
        return True
    else:
        temp = [(blue_y - d_y, blue_x - d_x), (red_y - d_y, red_x - d_x)]
        if temp[1] == red:
            table[red[0]][red[1]] += 1
        if temp not in visited:
            myQ.append(temp)
        return False

def solve(myMap, table, visited, blue, red, hole):
    myQ = deque()
    myQ.append([blue, red])
    while (len(myQ) != 0):
        print(myQ)
        temp = myQ.popleft()
        blue_y, blue_x = temp[0]
        red_y, red_x = temp[1]
        visited.append((temp))
        for i in range(4):
            new_red_y = red_y + dy[i]
            new_red_x = red_x + dx[i]
            new_blue_y = blue_y + dy[i]
            new_blue_x = blue_x + dx[i]
            if ([(new_blue_y, new_blue_x), (new_red_y, new_red_x)] not in visited) and (myMap[new_red_y][new_red_x] != "#" or myMap[new_blue_y][new_blue_x] != "#"):
                flag = go(myMap, table, visited, (blue_y, blue_x), (red_y, red_x), dy[i], dx[i], myQ)
                if flag:
                    return table[hole[0]][hole[1]]
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
            elif temp[j] == "O":
                hole = (i, j)

        myMap.append(temp)

    table = [[0 for _ in range(M)] for _ in range(N)]
    visited = []
    result = solve(myMap, table, visited, blue, red, hole)
    print(result)


if __name__ == "__main__":
    main()