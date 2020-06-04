import sys


def is_prime(number):
    for i in range(3, int(number ** (1 / 2)) + 1):
        if number % i == 0:
            return False
        else:
            continue
    return True


def solve(number):
    for b in range(number-3, number//2 - 1, -2):
        if is_prime(b):
            a = number - b
            if is_prime(a):
                return [a, b]
            else:
                continue
        else:
            continue
    return [0]


def main():
    while True:
        num = int(sys.stdin.readline().rstrip())
        if num == 0:
            break
        else:
            temp = solve(num)
            if len(temp) == 1:
                print("Goldbach's conjecture is wrong.")
            else:
                print("{} = {} + {}".format(num, temp[0], temp[1]))


if __name__ == "__main__":
    main()