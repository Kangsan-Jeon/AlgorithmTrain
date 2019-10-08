import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    lst = [int(x) for x in sys.stdin.readline().rstrip().split()]
    result = [-1 for _ in range(N)]
    mydeq = deque()
    mydeq.append((0, lst[0]))
    for i in range(1, N):
        temp = lst[i]
        if temp > mydeq[0][1]:
            while(len(mydeq) != 0):
                idx, _ = mydeq.pop()
                result[idx] = temp
            mydeq.append((i, temp))

        elif temp > mydeq[-1][1]:
            idx, _ = mydeq.pop()
            result[idx] = temp
            while(mydeq[-1][1] < temp):
                idx, _ = mydeq.pop()
                result[idx] = temp
        mydeq.append((i, temp))

    print(*result)

if __name__ == "__main__":
    main()
