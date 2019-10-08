import sys

string = sys.stdin.readline()
T = int(sys.stdin.readline())
leftStack = list(string.strip())
rightStack = []
for i in range(T):
    operator = sys.stdin.readline()
    operator = operator.split()
    oper = operator[0]
    if oper == "L":
        if (len(leftStack) != 0):
            rightStack.append(leftStack.pop())
    elif oper == "D":
        if (len(rightStack) != 0):
            leftStack.append(rightStack.pop())
    elif oper == "P":
        char = operator[1]
        leftStack.append(char)
    else:   # B
        if (len(leftStack) != 0):
            leftStack.pop()
result = ""
for x in leftStack:
    result += x
while (len(rightStack) != 0):
    result += rightStack.pop()
print(result)
