T = int(input())

def decode(str):
    if (str == '0001101'):
        return 0
    elif (str == '0011001'):
        return 1
    elif (str == '0010011'):
        return 2
    elif (str == '0111101'):
        return 3
    elif (str == '0100011'):
        return 4
    elif (str == '0110001'):
        return 5
    elif (str == '0101111'):
        return 6
    elif (str == '0111011'):
        return 7
    elif (str == '0110111'):
        return 8
    else:
        return 9

def isCorrcet(lst):
    a = (lst[0] + lst[2] + lst[4] + lst[6])*3 + (lst[1] + lst[3] + lst[5]) + lst[7]
    # print(a)
    if a % 10 == 0:
        return sum(lst)
    else:
        return 0

for i in range(T):
    lst = []
    N, M = input().split()
    # print(inp)
    N = int(N)
    M = int(M)
    j = 0
    while (j < N):
        line = input()
        if (line.find('1') != -1):
            string = line
        j+=1
    ind = len(string) - 1
    while (ind >= 0):
        if string[ind] == '1':
            break
        ind -= 1
    subStr = string[ind-55:ind+2]
    for k in range(0, 8):
        number_str = subStr[7*k:7*(k+1)]
        lst.append(decode(number_str))
    # print(lst)
    print("#{} {}".format(i + 1, isCorrcet(lst)))