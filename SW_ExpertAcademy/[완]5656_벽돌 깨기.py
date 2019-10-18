'''
Algorithm
[DFS, Simulation]
목표 : 모든 경우에 대해서 가장 적게 남은 블록의 개수를 구한다.
1. 처음에 구슬을 떨어뜨릴 때 깨지는 벽돌을 찾기 위해 table에 각 열에서 0의 개수를 저장한다.
ex) 문제 첫 번째 테스트 케이스의 경우 table = [1, 3, 1, 5, 1, 2, 5, 5, 4, 2]
2. 함수 dfs에서는 구슬을 떨어뜨리는 위치만 정해준다.
3. 실제 블럭이 깨지는 것은 breakBlock에서 구현하고 깨진 블럭을 재배열시키는 것은 arrange에서 구현한다.
=> 깨질 블럭을 stack에 추가하고 빼면서 주변 블럭을 깨지도록 구현한다.
=> arrange에서는 바뀐 map에 따라 table도  새로 구성한다.
'''

copyMap = []
copyTable= []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def arrange(myMap, table, W, H):
    for i in range(W):
        idx = H-1
        cnt = 0
        while (idx >= 0):
            if myMap[idx][i] == 0:
                cnt += 1
            else:
                if cnt != 0:
                    myMap[idx+cnt][i] = myMap[idx][i]
                    myMap[idx][i] = 0
            idx -= 1
        table[i] = cnt  # cnt = 0 -> table[i] = 0,
    return


def breakBlock(myMap, table, myStack, W, H):
    while myStack:
        x, y, num = myStack.pop()
        for i in range(4):
            for j in range(1, num):
                next_y = y + dy[i]*j
                next_x = x + dx[i]*j
                if next_y >= 0 and next_y < H and next_x >= 0 and next_x < W \
                        and myMap[next_y][next_x] != 0:
                    myStack.append((next_x, next_y, myMap[next_y][next_x]))
                    myMap[next_y][next_x] = 0
    arrange(myMap, table, W, H)
    return

def dfs(myMap, table, minBlock, W, H, N, n):
    '''
    n번째 구슬을 떨어뜨릴 때 myMap의 변화를 나타냄
    :param myMap: map
    :param table: empty space of each columns
    :param minBlock: minumum rest of block
    :param W: width of map
    :param H: height of map
    :param N: the number of bead to drop
    :param n: current number of bead
    :return: mibBlock
    '''
    if n == N + 1:
        return W*H - sum(table)

    else:
        for i in range(W):
            copyMap = [x[:] for x in myMap]
            copyTable = table[:]
            if table[i] != H:
                copyMap[table[i]][i] = 0
                breakBlock(copyMap, copyTable, [(i, table[i], myMap[table[i]][i])], W, H)
            temp = dfs(copyMap, copyTable, minBlock, W, H, N, n+1)
            minBlock = min(temp, minBlock)
        return minBlock

def solve(myMap, table, minBlock, W, H, N):
    result = dfs(myMap, table, minBlock, W, H, N, 1)
    return result


def main():
    T = int(input())
    for t in range(T):
        N, W, H = (int(x) for x in input().split())
        myMap = []
        table = [-1 for _ in range(W)]
        for i in range(H):
            temp = input().split()
            for j in range(W):
                temp[j] = int(temp[j])
                if temp[j] > 0 and table[j] == -1:
                    table[j] = i
            myMap.append(temp)

        minBlock = W*H - sum(table)
        result = solve(myMap, table, minBlock, W, H, N)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()