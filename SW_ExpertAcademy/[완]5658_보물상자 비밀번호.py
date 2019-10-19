from collections import deque

def convert(password):
    num = 0
    n = len(password)
    for i in range(n):
        temp = password[n-1-i]
        if temp == "A":
            num += 10*(16**i)
        elif temp == "B":
            num += 11*(16**i)
        elif temp == "C":
            num += 12*(16**i)
        elif temp == "D":
            num += 13*(16**i)
        elif temp == "E":
            num += 14*(16**i)
        elif temp == "F":
            num += 15*(16**i)
        else:
            num += int(temp)*(16**i)
    return num

def solve(myQ, N, K):
    n = N//4
    passwords = []
    for i in range(n):
        for j in range(4):
            password = []
            for k in range(n):
                password.append(myQ[j*n + k])
            num = convert(password)
            if num not in passwords:
                passwords.append(num)
        myQ.appendleft(myQ.pop())
    passwords.sort(reverse=True)
    return passwords[K-1]

def main():
    T = int(input())
    for t in range(T):
        N, K = (int(x) for x in input().split())
        myQ = deque(list(input()))
        result = solve(myQ, N, K)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()