def solution(numbers, target):
    answer = 0

    n = len(numbers)

    bfs = [0]

    for i in range(n):
        result = []
        while(len(bfs) != 0):
            temp = bfs.pop()
            result.append(temp + numbers[i])
            result.append(temp - numbers[i])
        bfs = result

    answer = bfs.count(target)
    return answer

print(solution([1, 1, 1, 1, 1], 3))