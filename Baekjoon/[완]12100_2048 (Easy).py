from collections import deque
from copy import deepcopy

'''
Algorithm
1. dfs 함수를 호출하면 방향에 따라 움직인다
2. 각 행과 열의 움직임의 결과는 getResult에서 반환하고 myMap은 move에서 갱신한다.
=> getResult는 row를 왼쪽으로 움직였을 때 merge한 결과로
    오른쪽으로 움직일 때는 row를 역순으로 저장한 뒤 결과를 다시 역순으로 myMap에 저장한다.
    (Ex. [4, 2, 2] move right의 결과([0, 4, 4])는 [2, 2, 4] move left의 결과([4, 4, 0])의 역순과 같다)
    위로 움직일 경우 column을 따로 deque으로 저장한 뒤 myMap을 갱신한다
    아래로 움직일 경우 column을 역순으로 저장한 뒤 결과를 다시 역순으로 myMap에 갱신한다.
3. 모든 움직임의 결과를 적용한 map은 move함수에서 반환한다.
3. k가 5가 되지 않았지만, myMap의 모든 숫자가 다를 때(check함수가 False를 반환할 때) 더 큰 숫자를 만들 수 없으므로 findMax를 호출한다.
4. k = 5이면 findMax를 통해 최대값을 반환한다.
'''

dx = [-1, 1, 0, 0]  # left, right, up, down
dy = [0, 0, -1, 1]

def findMax(myMap, N):
    myMax = 0
    for i in range(N):
        for j in range(N):
            myMax = max(myMax, myMap[i][j])
    return myMax

def check(myMap, N):
    values = []
    for i in range(N):
        for j in range(N):
            if myMap[i][j] != 0:
                if myMap[i][j] not in values:
                    values.append(myMap[i][j])
                else:
                    return True
    return False


def getResult(myDeq, N):
    result = deque()
    flag = True     # 더할 수 있는가 (이미 더한 결과이면 더 이상 더할 수 없기 때문)
    while myDeq:
        temp = myDeq.popleft()
        if temp != 0:
            if result:
                if result[-1] == temp and flag:
                    result.append(result.pop() * 2)
                    flag = False
                else:
                    result.append(temp)
                    flag = True
            else:
                result.append(temp)
    while (len(result) != N):
        result.append(0)
    return result


def move(myMap, direction, N):
    if direction == 0:      # Move Left
        for i in range(N):
            row = myMap[i]
            myMap[i] = getResult(row, N)

    elif direction == 1:    # Move right
        for i in range(N):
            row = [myMap[i][j] for j in range(N-1, -1, -1)]
            row = deque(row)
            temp_row = getResult(row, N)
            idx = 0
            while(idx < N):
                myMap[i][idx] = temp_row[N - idx -1]
                idx+=1

    elif direction == 2:    # Move up
        for i in range(N):
            col = []
            for j in range(N):
                col.append(myMap[j][i])
            col = deque(col)
            temp_col = getResult(col, N)
            idx = 0
            while(idx < N):
                myMap[idx][i] = temp_col[idx]
                idx+=1

    else:   # Move down
        for i in range(N):
            col = []
            for j in range(N-1, -1, -1):
                col.append(myMap[j][i])
            col = deque(col)
            temp_col = getResult(col, N)
            idx = 0
            while(idx < N):
                myMap[idx][i] = temp_col[N - idx - 1]
                idx+=1
    return myMap

def dfs(myMap, direction, k, N):
    if k == 5:
        return findMax(myMap, N)
    else:
        copyMap = deepcopy(myMap)
        copyMap = move(copyMap, direction, N)
        if check(copyMap, N):
            return max([dfs(copyMap, 0, k+1, N), dfs(copyMap, 1, k+1, N),
                        dfs(copyMap, 2, k+1, N), dfs(copyMap, 3, k+1, N)])
        else:
            return findMax(copyMap, N)

def solve(myMap, N):
    myMax = 0
    for i in range(4):
        myMax = max(myMax, dfs(myMap, i, 0, N))
    return myMax

def main():
    N = int(input())
    myMap = []
    for i in range(N):
        temp = [int(x) for x in input().split()]
        myMap.append(deque(temp))

    print(solve(myMap, N))

if __name__ == "__main__":
    main()