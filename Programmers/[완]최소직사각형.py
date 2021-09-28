'''
1. 각 명함 사이즈마다 더 긴 길이는 longer_max와 더 짧은 길이는 shorter_max와 각각 비교한다.
2. answer = 더 긴 변의 max * 더 짧은 변의 max
'''

def solution(sizes):
    longer_max = 0
    shorter_max = 0
    for size in sizes:
        longer_max = max(max(size), longer_max)
        shorter_max = max(min(size), shorter_max)
    answer = longer_max*shorter_max
    return answer


examples = [
    [[60, 50], [30, 70], [60, 30], [80, 40]],
    [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]],
    [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]],
]

for example in examples:
    print(solution(example))