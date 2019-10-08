def isLarger(priorities, number):
    # print(number)
    for x in priorities:
        if x > number:
            return True
    return False

def solution(priorities, location):
    answer = 0
    cnt = 1
    while ( len(priorities) != 0):
        # print(priorities)
        if isLarger(priorities, priorities[0]):
            temp = priorities.pop(0)
            priorities.append(temp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        else:
            priorities.pop(0)
            if location == 0:
                answer = cnt
                break

            else:
                location -= 1
            cnt += 1


    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))