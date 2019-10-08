import sys
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def checkBox(boxes, M, N, H):
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if boxes[h][i][j] == 0:
                    return False
    return True

def solve(boxes, table, myQ, M, N, H):
    time = 0
    while (len(myQ) != 0):
        y, x, z = myQ.popleft()
        time = table[z][y][x]
        for i in range(6):
            new_x = x + dx[i]
            new_y = y + dy[i]
            new_z = z + dz[i]
            if new_x >= 0 and new_x < M and new_y >= 0 and new_y < N and new_z >= 0 and new_z < H:
                if boxes[new_z][new_y][new_x] == 0:
                    table[new_z][new_y][new_x] = time + 1
                    boxes[new_z][new_y][new_x] = 1
                    myQ.append((new_y, new_x, new_z))

    if checkBox(boxes, M, N, H):
        result = time
    else:
        result = -1
    return result

def main():
    M, N, H = (int(x) for x in sys.stdin.readline().rstrip().split())
    boxes = []
    myQ = deque()
    table = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]
    for h in range(H):
        box = []
        for i in range(N):
            line = []
            temp = sys.stdin.readline().rstrip().split()
            for j in range(len(temp)):
                temp_num = int(temp[j])
                line.append(temp_num)
                if temp_num == 1:
                    table[h][i][j] = 0
                    myQ.append((i, j, h))
            box.append(line)
        boxes.append(box)
    result = solve(boxes, table, myQ, M, N, H)
    print(result)

if __name__ == "__main__":
    main()