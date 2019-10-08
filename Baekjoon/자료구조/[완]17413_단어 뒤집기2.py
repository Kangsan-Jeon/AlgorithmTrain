import sys


def main():
    line = sys.stdin.readline().rstrip()
    n = len(line)
    ind = 0
    result = ""
    myStack = []
    while(ind < n):
        temp = line[ind]
        if temp == " ":
            while(len(myStack) != 0):
                result += myStack.pop()
            result += " "
        elif temp == "<":
            while(len(myStack) != 0):
                result += myStack.pop()
            while (line[ind] != ">"):
                result += line[ind]
                ind += 1
            result += line[ind]
        else:
            myStack.append(temp)
        ind += 1
    while(len(myStack) != 0):
        result += myStack.pop()
    print(result)

if __name__ == "__main__":
    main()