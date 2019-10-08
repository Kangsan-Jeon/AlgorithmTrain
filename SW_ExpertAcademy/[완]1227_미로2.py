import queue
n = 100

# DFS
def dfs(arr, path):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    while (len(path) != 0):
        x, y = path[-1]
        path = path[:-1]
        if arr[y][x] == 4:
            continue
        elif arr[y][x] == 3:
            return True
        else:
            arr[y][x] = 4  # visited position
            for i in range(4):
                temp_x = x + dx[i]
                temp_y = y + dy[i]
                if (temp_x < 0 or temp_x >= n or temp_y <0 or temp_y >= n ):
                    continue
                else:
                    value = arr[temp_y][temp_x]
                    if (value == 0 or value == 3):
                        path.append((temp_x, temp_y))
    return False

for t in range(10):
    T = int(input())
    arr = []

    # make array
    for i in range(n):
        line = input()
        row = []
        for j in range(n):
            temp = int(line[j])
            if temp == 2:
                start = (j, i)
            row.append(temp)
        arr.append(row)

    path = [start]
    result = dfs(arr, path)

    if (result):
        print("#{} 1".format(T))
    else:
        print("#{} 0".format(T))
