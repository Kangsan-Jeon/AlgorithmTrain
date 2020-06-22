import sys


def solve(n, arr):
    '''
    table[i] = arrr[i]를 포함했을 때 가장 긴 증가하는 부분 수열의 길이
    '''
    table = [1 for _ in range(n)]
    temp = [str(arr[i]) for i in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                if table[i] < table[j] + 1:
                    table[i] = table[j] + 1
                    temp[i] = temp[j] + " " + str(arr[i])
    max_len = max(table)
    idx = table.index(max_len)
    max_arr = temp[idx]
    return max_len, max_arr


def main():
    N = int(sys.stdin.readline())
    arr = [int(x) for x in sys.stdin.readline().split()]
    max_len, max_arr = solve(N, arr)
    print(max_len)
    print(max_arr)


if __name__ == "__main__":
    main()