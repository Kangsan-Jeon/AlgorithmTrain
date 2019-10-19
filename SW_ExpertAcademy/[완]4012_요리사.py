'''
Algorithm
1. makeCase를 통해 가능한 경우의 수를 모두 구한다.
2. 가능한 경우의 수에 대해 calTaste로 음식의 맛을 계산하고 차의 최소값을 갱신한다.
'''

def makeCase(N):
    case = [[[0], []]]
    for i in range(1, N):
        newCase = []
        while(len(case) != 0):
            temp = case.pop()
            if len(temp[0]) < N/2:
                newCase.append([temp[0] + [i], temp[1]])
            if len(temp[1]) < N/2:
                newCase.append([temp[0], temp[1] + [i]])
        case = newCase
    return case

def calTaste(synergy, foods):
    n = len(foods)
    taste = 0
    for i in range(n):
        f1 = foods[i]
        for j in range(i+1, n):
            f2 = foods[j]
            taste = taste + synergy[f1][f2] + synergy[f2][f1]
    return taste

def solve(synergy, N):
    cases = makeCase(N)
    minDiff = 320001
    for case in cases:
        a = case[0]
        b = case[1]
        taste_a = calTaste(synergy, a)
        taste_b = calTaste(synergy, b)
        minDiff = min(abs(taste_a - taste_b), minDiff)
    return minDiff

def main():
    T = int(input())

    for t in range(T):
        N = int(input())
        synergy = []
        for i in range(N):
            temp = [int(x) for x in input().split()]
            synergy.append(temp)
        result = solve(synergy, N)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()