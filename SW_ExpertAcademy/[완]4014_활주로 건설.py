'''
Algorithm
1. 각 행과 열에 대하여 가장 높은 곳의 인덱스의 왼쪽과 오른쪽을 체크한다.
=> 각 행과, 열에 대하여 가장 크기가 큰 수의 인덱스를 rowMaxIdx 와 colMaxIdx에 저장
=> 가장 높은 곳이 이어진 경우 끝날 때 부터의 리스트를 입력으로 한다.
=> left는 오른쪽 끝부터, right는 왼쪽 끝부터 탐색한다.
ex) [1, 2, 2, 3, 4, 5, 5, 5, 4] 의 경우 left = [1, 2, 2, 3, 4], right = [4]
2. 이전의 높이와 차가 2 이상 날 경우 check함수는 False를 반환한다.
3. 이전의 높이가 1 더 높은 경우 아직 경사로를 설치하지 못했으면 False를 반환한다.
※ 만약 left일 때 i가 n-1이고, right일 때 i = 0인 경우는 제외.
   이때는 이후의 length의 길이에 따라 통해 활주로의 설치 유무가 달라진다.
ex) maxNum = 5, X = 2이고 left = [3, 3, 4] 일 때 높이가 4에서 3으로 변할 때
경사로를 설치하지 못했으므로 False를 반환한다.
4. 이전의 높이가 1 더 작은 경우 이전의 높이가 얼마나 이어졌냐에 따라 경사로를 설치할 수 있다.
ex) maxNum = 4, X = 2, left = [4, 3, 3, 3, 3, 3, 4, 4] 일 때 높이가 3에서 4로 변할 때(index = 0)
    3이 X이상 이어져 왔으므로 경사로를 설치할 수 있다.
※ 높이가 4에서 3으로 변할 때(index = 5) 경사로를 설치하는 경우를 고려하여 length를 설정해야 한다.
   즉 index가 4와 5인 지점은 경사로를 설치해야 하므로 index = 0일 때 3이 이어진 length는 3이다.
5. checkLeft와 checkRight가 모두 True이면 경우의 수를 나타내는 num을 1 증가시킨다.
'''

def checkLeft(left, maxNum, X):
    '''
    :param left: 가장 높은 곳의 왼쪽 부분
    :param maxNum: 가장 높은 곳의 높이
    :param X: 활주로 길이
    :return: 활주로가 이어지면 True, 그렇지 않으면 Fasle
    '''
    n = len(left)
    if n == 0:
        return True
    else:
        pre_num = maxNum
        length = 0
        flag = False  # 경사로를 세웠니?

        for i in range(n - 1, -1, -1):
            if pre_num == left[i]:
                length += 1
                if not flag:
                    if length == X:
                        length = 0
                        flag = True
            else:
                if pre_num - left[i] == 1:
                    if (not flag) and i != n-1:
                        return False
                    pre_num = left[i]
                    length = 1
                    flag = False

                elif pre_num - left[i] == -1:
                    if X > length:
                        return False
                    pre_num = left[i]
                    length = 1
                    flag = True
                else:
                    return False
        if flag:
            return True
        else:
            return False

def checkRight(right, maxNum, X):
    '''
    :param right: 가장 높은 곳의 오른쪽 부분(높은 곳이 이어진다면 끝나는 부분부터)
    :param maxNum: 가장 높은 곳의 높이
    :param X: 활주로 길이
    :return: 활주로가 이어지면 True, 그렇지 않으면 Fasle
    '''
    n = len(right)
    if n == 0:
        return True
    else:
        pre_num = maxNum
        length = 0
        flag = False

        for i in range(0, n):
            if right[i] == pre_num:
                length += 1
                if not flag:
                    if length == X:
                        length = 0
                        flag = True
            else:
                if pre_num - right[i] == 1:
                    if (not flag) and (i != 0):
                        return False
                    pre_num = right[i]
                    length = 1
                    flag = False

                elif pre_num - right[i] == -1:
                    if X > length:
                        return False
                    pre_num = right[i]
                    length = 1
                    flag = True

                else:
                    return False
        if flag:
            return True
        else:
            return False


def solve(my_map, N, X, rowMaxIdx, colMaxIdx):
    '''
    :param my_map: map
    :param N: map의 크기
    :param X: 활주로의 크기
    :param rowMaxIdx: 각 행의 가장 높은 곳의 인덱스
    :param colMaxIdx: 각 열의 가장 높은 곳의 인덱스
    :return: 활주로를 설치할 수 있는 경우의 수
    '''
    num = 0 # 경우의 수
    for row in range(N):
        maxIdx = rowMaxIdx[row]
        maxNum = my_map[row][maxIdx]
        rightList = my_map[row][maxIdx+1:]
        idx = 0
        while (idx < len(rightList)):
            if rightList[idx] != maxNum:
                break
            idx += 1
        rightList = rightList[idx:]
        if checkLeft(my_map[row][:maxIdx], maxNum, X) and checkRight(rightList, maxNum, X):
            num += 1

    # check column direction
    for col in range(N):
        maxIdx = colMaxIdx[col]
        maxNum = my_map[maxIdx][col]
        upList = []
        downList = []
        flag = False
        for i in range(N):
            if i < maxIdx:
                upList.append(my_map[i][col])
            elif i > maxIdx:
                if maxNum > my_map[i][col]:
                    flag = True
                if flag:
                    downList.append(my_map[i][col])

        if checkLeft(upList, maxNum, X) and checkRight(downList, maxNum, X):
            num += 1
    return num

def main():
    T = int(input())
    for t in range(T):
        N, X = (int(x) for x in input().split())
        my_map = []
        rowMaxIdx = []
        colMaxIdx = []

        for i in range(N):
            myMax = 0
            temp = input().split()
            temp_idx = -1
            for j in range(N):
                temp[j] = int(temp[j])
                if temp[j] > myMax:
                    temp_idx = j
                    myMax = temp[j]
            rowMaxIdx.append(temp_idx)
            my_map.append(temp)

        for i in range(N):
            myMax = 0
            temp_idx = -1
            for j in range(N):
                if my_map[j][i] > myMax:
                    temp_idx = j
                    myMax = my_map[j][i]
            colMaxIdx.append(temp_idx)
        result = solve(my_map, N, X, rowMaxIdx, colMaxIdx)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()