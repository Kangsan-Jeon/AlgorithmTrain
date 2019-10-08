from collections import deque
import sys

def main():
    T = int(sys.stdin.readline())
    deq = deque()

    for t in range(T):
        inp = sys.stdin.readline().rstrip().split()
        oper = inp[0]
        n = len(deq)
        if oper == "push_back":
            x = int(inp[1])
            deq.append(x)

        elif oper == "push_front":
            x = int(inp[1])
            deq.appendleft(x)

        elif oper == "front":
            if n == 0:
                print(-1)
            else:
                temp = deq.popleft()
                deq.appendleft(temp)
                print(temp)

        elif oper == "back":
            if n == 0:
                print(-1)
            else:
                temp = deq.pop()
                deq.append(temp)
                print(temp)
        elif oper == "size":
            print(n)
        elif oper == "empty":
            if n==0:
                print(1)
            else:
                print(0)
        elif oper == "pop_front":
            if n == 0:
                print(-1)
            else:
                print(deq.popleft())
        else:   # pop_back
            if n==0:
                print(-1)
            else:
                print(deq.pop())

if __name__ == "__main__":
    main()