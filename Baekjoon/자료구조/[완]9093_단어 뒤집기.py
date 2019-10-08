T = int(input())

for i in range(T):
    myStack = []
    words = input().split()
    string = ""
    for word in words:
        for j in range(len(word)):
            myStack.append(word[j])
        while (len(myStack) != 0):
            string += myStack.pop()
        string += " "
    print(string)

