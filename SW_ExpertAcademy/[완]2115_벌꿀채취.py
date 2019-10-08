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
    result = result[1:]
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
                sumPower = 0
                sumHoney = 0
                idx = case[k]
                for x in idx:
                    sumHoney += temp[x]
                    sumPower += temp[x]**2
                if sumHoney <= C:
                    myMax = max(myMax, sumPower)
            table[i][j] = myMax
    return table

def solve(honey, N, M, C):
    table_col = N - M + 1
    '''
    table[i][j] : i행에서 j열 부터 M만큼까지 선택했을 때 최대 수익
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