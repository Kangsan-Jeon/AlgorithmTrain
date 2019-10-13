from collections import deque

dx = [-1, 1, 0, 0]  # left, right, up, down
dy = [0, 0, -1, 1]

def go(myMap, visited, blue, red, d_y, d_x, cnt, myQ):
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

    if blue_state:
        return 0

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
        return 0
    elif red_state:
        return cnt+1
    else:
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
                flag = go(myMap, visited, (blue_y, blue_x), (red_y, red_x), dy[i], dx[i], cnt, myQ)
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