'''
Algorithm : DP를 통해 접근
1. i행, j열에서 M만큼 선택가능할 때 발생하는 최대 수익을 table에 저장
=> table의 크기는 N x (N-M+1). ex) 3x3에서 M이 2일 때 (0~1열), (1~2열)을 선택 가능
2. table은 makeTable에서 반환
3. makeTable에서 최대 수익을 구하기 위해 makeCase에서 선택할 수 있는 경우를 모두 반환한다.
4. makeCase에서는 크기 M의 배열에서 선택가능한 인덱스를 반환한다
ex) M = 3 -> [[0], [1], [2], [0 , 1], [0, 2], [1, 2]]
5. 각 경우에 대해서 벌꿀의 양과 수익을 구하고 벌꿀의 양이 C 이하이고 수익이 최대 수익보다 크면 갱신
6. solve에서는 table을 돌아다니며 얻을 수 있는 최대 수익을 구한다.
=> 만약 person1이 (i, j)에서 (i, j+M-1)까지 선택했을 때 얻을 수 있는 최대 수익은
table[i][j]에 저장되므로 person2는 (i, j+M)부터 발생할 수 있는 최대 수익을 getMax를 통해 얻는다.
※ person1과 같은 행일 때 (j+M)열부터 table을 탐색해야한다. 다를 경우에는 전체 열에 대해서 탐색 가능하다.
'''

def getMax(table, row, col):
    N = len(table)
    M = len(table[0])
    myMax = 0
    for i in range(row, N):
        if i == row:
            for j in range(col, M):
                if table[i][j] > myMax:
                    myMax = table[i][j]
        else:
            for j in range(M):
                if table[i][j] > myMax:
                    myMax = table[i][j]
    return myMax

def makeCase(N):
    result = [[]]
    for i in range(N):
        for j in range(len(result)):
            result.append(result[j] + [i])
    result = result[1:] # result[0] = 빈 리스트
    return result

def makeTable(honey, N, M, C):
    table_len = N - M + 1
    table = [[0 for _ in range(table_len)] for _ in range(N)]
    for i in range(N):
        for j in range(table_len):
            temp = honey[i][j:j+M]
            myMax = 0
            case = makeCase(M)
            for k in range(len(case)):
                profit = 0
                sumHoney = 0
                idx = case[k]
                for x in idx:
                    sumHoney += temp[x]
                    profit += temp[x]**2
                if sumHoney <= C:
                    myMax = max(myMax, profit)
            table[i][j] = myMax
    return table

def solve(honey, N, M, C):
    table_col = N - M + 1
    '''
    table[i][j] : i행, j열부터 시작하여 M만큼까지 선택했을 때 최대 수익
    '''
    table = makeTable(honey, N, M, C)
    # print(table)
    result = 0
    for i in range(N):
        for j in range(table_col):
            person1 = table[i][j]
            result = max(result, person1 + getMax(table, i, j+M))
    return result

def main():
    T = int(input())
    for t in range(T):
        N, M, C = (int(x) for x in input().split())
        honey = []
        for i in range(N):
            temp = [int(x) for x in input().split()]
            honey.append(temp)
        result = solve(honey, N, M, C)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()