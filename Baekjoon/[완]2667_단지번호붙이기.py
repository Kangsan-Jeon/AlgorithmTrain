dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def grouping(arr, x, y, n):
    bfs = [(x, y)]
    cnt = 0
    while (len(bfs) != 0):
        x, y = bfs.pop(0)
        if arr[y][x] == 1:
            cnt += 1
        else:
            continue
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < n:
                temp = arr[new_y][new_x]
                if temp == 1:
                    bfs.append((new_x, new_y))
        arr[y][x] = -1
    return arr, cnt



def getGroupNum(arr, n):
    result = []
    num = 0
    for row in range(n):
        for col in range(n):
            if arr[row][col] == 1:
                arr, cnt = grouping(arr, col, row, n)
                result.append(cnt)
                num+=1
    return result, num

if __name__ == "__main__":
    N = int(input())
    arr = []
    for i in range(N):
        temp = []
        line = input()
        for j in range(N):
            temp.append(int(line[j]))
        arr.append(temp)

    result, num = getGroupNum(arr, N)
    result.sort()
    print(num)
    for i in result:
        print(i)