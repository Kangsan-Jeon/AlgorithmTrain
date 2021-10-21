
'''
1. 모든 직선에 대해 교점을 구한다.
    - 직선 중 두 개를 선택하는 조합의 순서쌍을 구한다.
    - 교점이 정수인 것들만 저장한다.
    - 교점 중 x의 최소 및 최대, y의 최소 및 최대를 구한다.
2. 격자판의 가로 = minimum_x ~ maximum_x, 격자판의 세로 = minimum_y ~ maximum_y
    - 교점들을 grid의 좌표로 변환. (x, y) -> (c, r)
        Ex) (4, 1) -> (8, 3), (0, 4) -> (4, 0), (4, -4) -> (8, 8)
    - 변환된 교점들의 좌표의 "."은 "*"로 교체한다.
3. 각 row들은 join을 통해 문자열로 변환한다.
'''
def get_intersection(line_1, line_2):
    '''
    A1x + B1y + C1 = 0
    A2x + B2y + C2 = 0
    => x = -(C1*B2-C2*B1)/(A1*B2-A2*B1), y = -(C1*A2-C2*A1)/(B1*A2-B2*A1)
    '''
    int_intersection = None
    A1, B1, C1 = line_1
    A2, B2, C2 = line_2
    if (A1*B2-A2*B1) == 0:
        pass
    else:
        x = -(C1*B2-C2*B1)/(A1*B2-A2*B1)
        y = -(C1*A2-C2*A1)/(B1*A2-B2*A1)
        if x == int(x) and y == int(y):
            int_intersection = (int(x), int(y))

    return int_intersection

def solution(line):
    n = len(line)
    int_intersections = []
    min_x = 1001
    max_x = -1001
    min_y = 1001
    max_y = -1001
    x_list = []
    y_list = []
    for i in range(n):
        for j in range(i+1, n):
            intersection = get_intersection(line[i], line[j])
            if intersection is None:
                continue
            else:
                x_list.append(intersection[0])
                y_list.append(intersection[1])
                int_intersections.append(intersection)

    min_x = min(x_list)
    max_x = max(x_list)
    min_y = min(y_list)
    max_y = max(y_list)
    grid = [["." for _ in range(max_x-min_x+1)] for _ in range(max_y-min_y+1)]
    for x, y in int_intersections:
        grid[max_y-y][x-min_x] = "*"
    answer = ["".join(row) for row in grid]
    return answer

examples = [
    [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]],
    [[0, 1, -1], [1, 0, -1], [1, 0, 1]],
    [[1, -1, 0], [2, -1, 0]],
    [[1, -1, 0], [2, -1, 0], [4, -1, 0]],
    [[1, -1, 2], [2, -1, 2], [3, -1, 2], [4, -1, 2], [5, -1, 2], [6, -1, 2], [-1, -1, 2]]
]

for example in examples:
    print(solution(example))