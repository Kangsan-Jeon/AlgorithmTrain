from collections import deque

# 전체 경우의 수를 구하기 위해 이전까지 모든 경우 + 현재 stair1으로 갈 때, stair2로 갈 때
def appendCase(case, d1, d2):
    n = len(case)
    new_case = []
    for i in range(n):
        s1, s2 = case[i]
        new_s1 = s1 + [d1]
        new_s2 = s2 + [d2]
        new_case.append((new_s1, s2))
        new_case.append((s1, new_s2))
    return new_case

# 전체 경우의 수를 구한다(stair1을 모두가 이용할 경우 ~ stair2f를 모두가 이용할 경우)
def makeCase(people, stairs):
    p_y, p_x = people[0]
    s1_y, s1_x = stairs[0]
    s2_y, s2_x = stairs[1]
    # case = [[(stair1을 이용하는 사람이 계단을 내려갈 수 있는 시간), (stair2를 이용하는 사람이 계단을 내려갈 수 있는 시간)], ...]
    case = [([abs(p_y - s1_y) + abs(p_x - s1_x) + 1], []),
            ([], [abs(p_y - s2_y) + abs(p_x - s2_x) + 1])]
    for i in range(1, len(people)):
        p_y, p_x = people[i]
        d1 = abs(p_y - s1_y) + abs(p_x - s1_x) + 1
        d2 = abs(p_y - s2_y) + abs(p_x - s2_x) + 1
        case = appendCase(case, d1, d2)
    return case

def solve(s1, s2, k1, k2, minTime):
    s1.sort()
    s2.sort()
    n1 = len(s1)
    n2 = len(s2)
    stair1 = deque()
    stair2 = deque()
    t = 0
    time1 = 0
    time2 = 0
    idx1 = 0
    idx2 = 0
    while (idx1 < n1 or idx2 < n2):
        if t > minTime:
            return minTime
        while (len(stair1) != 0):
            if stair1[0] == t:
                time1 = stair1.popleft()
            else:
                break

        while (len(stair2) != 0):
            if stair2[0] == t:
                time2 = stair2.popleft()
            else:
                break

        if idx1 < n1:
            if s1[idx1] <= t:
                if len(stair1) == 3:
                    s1[idx1] += 1
                else:
                    stair1.append(max(s1[idx1], t) + k1)
                    idx1 += 1
                    while(idx1 < n1):
                        if len(stair1) == 3 or s1[idx1] > t:
                            break
                        stair1.append(max(s1[idx1], t) + k1)
                        idx1 += 1

        if idx2 < n2:
            if s2[idx2] <= t:
                if len(stair2) == 3:
                    s2[idx2] += 1
                else:
                    stair2.append(max(s2[idx2], t) + k2)
                    idx2 += 1
                    while(idx2 < n2):
                        if len(stair2) == 3 or s2[idx2] > t:
                            break
                        stair2.append(max(s2[idx2], t) + k2)
                        idx2 += 1
        t += 1

    while (len(stair1) != 0):
        time1 = stair1.popleft()
    while (len(stair2) != 0):
        time2 = stair2.popleft()

    return max(time1, time2)


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        graph = []
        people = []
        stairs = []
        minTime = 99999999999999
        for i in range(N):
            row = []
            temp = input().split()
            for j in range(N):
                num = int(temp[j])
                row.append(num)
                if num == 1:
                    people.append((i, j))
                elif num > 1:
                    stairs.append((i, j))
            graph.append(row)

        case = makeCase(people, stairs)
        k1 = graph[stairs[0][0]][stairs[0][1]]
        k2 = graph[stairs[1][0]][stairs[1][1]]

        for s1, s2 in case:
            time = solve(s1, s2, k1, k2, minTime)
            minTime = min(time, minTime)

        print("#{} {}".format(t+1, minTime))

if __name__ == "__main__":
    main()