import sys


table = [[-1, -1, -1] for _ in range(100001)]
# table[i][j] : 1, 2, 3을 더해 i를 맞출 때, (j+1) 로 시작하는 경우
table[1] = [1, 0, 0]  # 1
table[2] = [0, 1, 0]  # 2
table[3] = [1, 1, 1]  # 1+2+1, 2+1, 3


def solve(n):
    '''
    table[4][0] = table[3][1] + table[3][2]
    table[4][1] = table[2][0] + table[2][2]
    table[4][2] = table[1][0] + table[1][1]
    '''
    if sum(table[n]) != -3:
        return sum(table[n])
    else:
        for i in range(4, n + 1):
            if sum(table[i]) != -3:
                continue
            else:
                table[i] = [(table[i - 1][1] + table[i - 1][2]) % 1000000009,
                            (table[i - 2][0] + table[i - 2][2]) % 1000000009,
                            (table[i - 3][0] + table[i - 3][1]) % 1000000009]
        return sum(table[n])


def main():
    T = int(sys.stdin.readline())
    for _ in range(T):
        n = int(sys.stdin.readline())
        answer = solve(n) % 1000000009
        print(answer)


if __name__ == "__main__":
    main()
