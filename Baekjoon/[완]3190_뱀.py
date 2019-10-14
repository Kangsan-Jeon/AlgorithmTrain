from collections import deque
'''
Algorithm
[시뮬레이션]
1. 매 초마다 뱀의 위치를 snake라는 deque에 저장한다.
=> state[0]이 꼬리, state[-1]이 머리
2. 진행 방향을 바꿀 때를 고려하여 state 및 dx와 dy를 설정한다.
※ 뱀은 진행 방향을 t초 이후 바꾸므로 이를 고려한다.
=> state[0]이 현재의 진행 방향
=> 진행 방향이 Right일 때 왼쪽으로 진로를 변경하면 진향방향은 Up이고 오른쪽으로 변경하면 Down이므로 이에 맞게 state를 설정
    Ex) 진행방향이 Right일 때 왼쪽으로 변경시 Up이므로 state[-1]을 0번 인덱스로 넘긴다.
        오른쪽으로 변경시 Down이므로 state[1]을 0번 인덱스로 넘긴다.
3. 뱀의 이동할 때 다음 경로를 snake의 마지막에 추가한다.
4. 경로에 사과가 있을 경우 꼬리는 그대로 두고 사과가 없으면 popleft를 한다.
5. 다음 경로에 벽이 있거나 자신과 겹치면 move는 False를 반환하여 t 반환
'''
state = deque([0, 1, 2, 3])     # [R, D, L, U]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def move(myMap, snake, cur_dir):
    N = len(myMap)
    head_y, head_x = snake[-1]

    next_y = head_y + dy[cur_dir]
    next_x = head_x + dx[cur_dir]
    if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
        box = myMap[next_y][next_x]
        myMap[next_y][next_x] = 1
        snake.append((next_y, next_x))
        if box == 2:
            if myMap[next_y][next_x] == 2:
                myMap[next_y][next_x] = 0
        elif box == 0:
            tail_y, tail_x = snake.popleft()
            myMap[tail_y][tail_x] = 0
        else:
            return False
    else:
        return False
    return True

def solve(myMap, snake, moveList):
    t = 1
    while(1):
        if len(moveList) != 0 and moveList[0][0] + 1 == t:
            _, direction = moveList.popleft()
            if direction == "L":
                state.appendleft(state.pop())
            else:
                state.append(state.popleft())
        cur_dir = state[0]
        if move(myMap, snake, cur_dir):
            t += 1
        else:
            break

    return t

def main():
    N = int(input())
    K = int(input())
    myMap = [[0 for _ in range(N)] for _ in range(N)]
    for k in range(K):
        y, x = (int(x) for x in input().split())
        myMap[y-1][x-1] = 2
    L = int(input())
    moveList = deque()
    for l in range(L):
        temp = input().split()
        temp[0] = int(temp[0])
        moveList.append(temp)
    myMap[0][0] = 1
    snake = deque()    # [head, tail]
    snake.append((0, 0))
    result = solve(myMap, snake, moveList)
    print(result)


if __name__ == "__main__":
    main()