import sys

def main():
    N = int(sys.stdin.readline())
    expression = sys.stdin.readline().rstrip()
    myDict = dict()
    myStack = []

    for i in range(N):
        temp = int(sys.stdin.readline())
        myDict[chr(65+i)] = temp

    idx = 0

    for i in range(len(expression)):
        char = expression[i]
        if char == '*':
            oper2 = myStack.pop()
            oper1 = myStack.pop()
            myStack.append(oper1*oper2)
        elif char == '+':
            oper2 = myStack.pop()
            oper1 = myStack.pop()
            myStack.append(oper1 + oper2)
        elif char == '-':
            oper2 = myStack.pop()
            oper1 = myStack.pop()
            myStack.append(oper1 - oper2)
        elif char == '/':
            oper2 = myStack.pop()
            oper1 = myStack.pop()
            myStack.append(round(oper1/oper2, 2))
        else:
            myStack.append(myDict[char])

    print("{:.2f}".format(myStack[0]))

if __name__ == "__main__":
    main()