from collections import deque
import sys

def main():
    N, K = (int(x) for x in sys.stdin.readline().rstrip().split())
    que = deque()
    for i in range(1, N+1):
        que.append(i)
    idx = 1
    print("<", end = "")
    while (len(que)):
        if idx%K == 0:
            if len(que) == 1:
                print(que.popleft(), end=">")
            else:
                print(que.popleft(), end=", ")
        else:
            que.append(que.popleft())
        idx += 1


if __name__ == "__main__":
    main()