import sys


def main():
    line = sys.stdin.readline().rstrip()
    n = len(line)
    idx = 0
    cnt = 0
    myStack = []
    num_stick = []
    result = 0
    while (idx < n):
        if line[idx] == "(":
            if line[idx+1] == ")":
                idx += 1
                if len(myStack) != 0:
                    for i in range(len(myStack)):
                        num_stick[i] += 1

            else:
                myStack.append(line[idx])
                num_stick.append(0)
        else:
            myStack.pop()
            result += num_stick.pop() + 1
        idx += 1
    print(result)


if __name__ == "__main__":
    main()