from collections import deque
'''
Algorithm
1. 시계 방향으로 회전할 경우 리스트의 끝이 앞으로 이동, 반시계 방향은 리스트의 처음이 끝으로 이동 => 자료구조는 덱을 사용한다.
2. 돌리는 행위에 대한 변수는 큐에 저장한다.(코드에서는 덱을 사용)
3. 큐에 저장 된 것을 하나씩 pop하면서 명령을 수행한다.
=> 명령을 수행할 때 어떤 자석도 함께 돌아가는지 확인해야 하므로 check 함수를 통해 회전하는 자석을 반환한다.
=> 자석의 인덱스 2와 6을 비교했을 때 극이 다르면 회전하는데, 옆 자석의 회전 방향은 돌리는 방향의 반대이므로 -1을 곱해준다.
=> result에는 4개의 자석이 회전하는 방향을 저장한다.(0 : 회전X, 1 : 시계방향, -1 : 반시계방향)
=> 회전방향에 따라 rotate함수를 통해 해당 자석을 회전한다.
4. 전체 명령 수행 결과에 대해서 점수를 계산한다.
=> score = mag1[0] + mag2[0]*2 + mag3[0]*4 + mag4[0]*8
'''
def check(mag1, mag2, mag3, mag4, num, rotation):
    result = [0, 0, 0, 0]
    result[num-1] = rotation
    if num == 1:
        # right dirction
        if mag1[2] != mag2[6]:
            result[1] = result[0]*(-1)
            if mag2[2] != mag3[6]:
                result[2] = result[1]*(-1)
                if mag3[2] != mag4[6]:
                    result[3] = result[2]*(-1)
    if num == 2:
        # right direction
        if mag2[2] != mag3[6]:
            result[2] = result[1]*(-1)
            if mag3[2] != mag4[6]:
                result[3] = result[2]*(-1)
        # left direction
        if mag2[6] != mag1[2]:
            result[0] = result[1]*(-1)

    if num == 3:
        # right direction
        if mag3[2] != mag4[6]:
            result[3] = result[2]*(-1)
        # left direction
        if mag3[6] != mag2[2]:
            result[1] = result[2]*(-1)
            if mag2[6] != mag1[2]:
                result[0] = result[1]*(-1)

    if num == 4:
        # left direction
        if mag4[6] != mag3[2]:
            result[2] = result[3]*(-1)
            if mag3[6] != mag2[2]:
                result[1] = result[2]*(-1)
                if mag2[6] != mag1[2]:
                    result[0] = result[1]*(-1)
    return result

def rotate(mag, rotation):
    if rotation == 0:
        return mag
    elif rotation == 1:
        mag.appendleft(mag.pop())
    else:
        mag.append(mag.popleft())
    return mag

def solve(mag1, mag2, mag3, mag4, order):
    score = 0
    while (len(order) != 0):
        num, rotation = order.popleft()
        rotations = check(mag1, mag2, mag3, mag4, num, rotation)
        mag1 = rotate(mag1, rotations[0])
        mag2 = rotate(mag2, rotations[1])
        mag3 = rotate(mag3, rotations[2])
        mag4 = rotate(mag4, rotations[3])
    score += mag1[0]
    score += mag2[0]*2
    score += mag3[0]*4
    score += mag4[0]*8
    return score

def main():
    T = int(input())
    for t in range(T):
        K = int(input())
        magnet1 = deque([int(x) for x in input().split()], maxlen=8)
        magnet2 = deque([int(x) for x in input().split()], maxlen=8)
        magnet3 = deque([int(x) for x in input().split()], maxlen=8)
        magnet4 = deque([int(x) for x in input().split()], maxlen=8)
        order = deque()
        for i in range(K):
            num, rotation = (int(x) for x in input().split())
            order.append((num, rotation))
        result = solve(magnet1, magnet2, magnet3, magnet4, order)
        print("#{} {}".format(t+1, result))



if __name__ == "__main__":
    main()