import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    line = [int(x) for x in sys.stdin.readline().rstrip().split()]
    myDeq = deque()
    myDict = {}
    for i in range(N):
        temp = line[i]
        if  temp in myDict.keys():
            myDict[temp] += 1
        else:
            myDict[temp] = 1

    result = [-1 for _ in range(N)]

    myDeq.append((0, line[0], myDict[line[0]]))

    for i in range(1, N):
        value = line[i]
        cnt = myDict[value]
        if cnt > myDeq[0][2]:
            while (len(myDeq) != 0):
                idx, val, c = myDeq.pop()
                result[idx] = value
        elif cnt > myDeq[-1][2]:
            while (myDeq[-1][2] < cnt):
                idx, val, c = myDeq.pop()
                result[idx] = value
        myDeq.append((i, value, cnt))

    print(*result)

if __name__ == "__main__":
    main()