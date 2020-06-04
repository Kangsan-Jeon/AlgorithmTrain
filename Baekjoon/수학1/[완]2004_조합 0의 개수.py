import sys

'''
nCm = n!/m!/(n-m)!
nCm을 (n*(n-1)*...*(n-m+1))/m! 로 계산하려면 2나 5의 거듭제곱의 개수를 구하기 어려움

n!에서 5의 거듭제곱의 개수는
n//5 + n//(5^2) + n//(5^3) + ...
'''


def numOfaliquot(num, aliquot):
    count = 0
    idx = 1
    while num >= aliquot ** idx:
        count += num // (aliquot ** idx)
        idx += 1
    return count


def combination(n, m):
    num_of_ten = min(numOfaliquot(n, 5) - numOfaliquot(m, 5) - numOfaliquot(n - m, 5),
                     numOfaliquot(n, 2) - numOfaliquot(m, 2) - numOfaliquot(n - m, 2))
    return num_of_ten


def main():
    n, m = [int(x) for x in sys.stdin.readline().rstrip().split()]
    answer = combination(n, m)
    print(answer)


if __name__ == "__main__":
    main()
