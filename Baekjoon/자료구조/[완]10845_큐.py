import sys

class que():
    def __init__(self, maxSize=10000):
        self.size = 0
        self.f = 0
        self.r = 0
        self.myQueue = [0]*(maxSize + 1)
        self.maxSize = maxSize + 1
    def push(self, x):
        self.myQueue[self.f] = x
        self.f = (self.f+1)%self.maxSize
        self.size += 1
    def pop(self):
        if self.empty():
            return -1
        else:
            temp = self.myQueue[self.r]
            self.r = (self.r+1)%self.maxSize
            self.size -= 1
            return temp
    def empty(self):
        if self.r == self.f:
            return 1
        else:
            return 0

    def getSize(self):
        return self.size

    def front(self):
        if self.empty():
            return -1
        else:
            return self.myQueue[self.r]
    def back(self):
        if self.empty():
            return -1
        else:
            return self.myQueue[self.f-1]

def main():
    myqueue = que()
    T = int(sys.stdin.readline())
    for t in range(T):
        inp = sys.stdin.readline().split()
        oper = inp[0]
        if oper == "push":
            x = int(inp[1])
            myqueue.push(x)
        elif oper == "front":
            print(myqueue.front())
        elif oper == "back":
            print(myqueue.back())
        elif oper == "size":
            print(myqueue.getSize())
        elif oper == "empty":
            print(myqueue.empty())
        else:   # pop
            print(myqueue.pop())

if __name__ == "__main__":
    main()


