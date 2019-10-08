open_set = ['(', '{', '[', '<']
close_set = [')', '}', ']', '>']


if __name__ == "__main__":
    for t in range(1, 11):
        N = int(input())
        line = list(input())
        stack = []
        ind = 0
        while (ind < N):
            temp = line[ind]
            if temp in open_set:
                stack.append(temp)
            else:
                for i in range(4):
                    if temp == close_set[i]:
                        if stack[-1] == open_set[i]:
                            stack.pop()
                        else:
                            stack.append(temp)
            ind += 1

        # print(stack)
        if len(stack) != 0:
            print("#{} 0".format(t))
        else:
            print("#{} 1".format(t))

