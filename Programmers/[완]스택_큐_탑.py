def solution(heights):
    answer = []
    n = len(heights)
    for i in range(n):
        flag = True
        temp = heights[i]
        for j in range(i-1, -1, -1):
            if temp < heights[j]:
                flag = False
                answer.append(j+1)
                break
        if flag:
            answer.append(0)

    return answer


'''
def solution(heights):
    answer = []
    n = len(heights)
    prev = []
    for i in range(n):
        flag = True
        temp = heights.pop(0)
        m = len(prev)
        for j in range(m-1, -1, -1):
            if prev[j] > temp:
                answer.append(j+1)
                flag = False
                break
        if flag:
            answer.append(0)
        prev.append(temp)

    return answer
'''

print(solution([6, 9, 5, 7, 4]))
print(solution([3,9,9,3,5,7,2]))
print(solution([1,5,3,6,7,6,5]))