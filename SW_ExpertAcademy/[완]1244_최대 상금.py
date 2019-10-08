T = int(input())

def swap(numList):
    result = []
    for number in numList:
        num = list(number)
        for i in range(len(num) - 1):
            for j in range(i+1, len(num)):
                num_copy = num.copy()
                str = ""
                temp = num_copy[i]
                num_copy[i] = num_copy[j]
                num_copy[j] = temp
                for char in num_copy:
                    str+=char
                if  result.count(str) == 0:
                    result.append(str)
    return result


for i in range(T):
    numList = []
    numStr, cnt = input().split()
    cnt = int(cnt)
    numList.append(numStr)
    for j in range(cnt):
        numList = swap(numList)
    # print(numList)
    max = 0
    for num in numList:
        length = len(numList[0]) - 1
        number = 0
        for k in num:
            number += int(k)*10**(length)
            length -= 1
        if max < number:
            max = number
    print("#{} {}".format(i+1, max))