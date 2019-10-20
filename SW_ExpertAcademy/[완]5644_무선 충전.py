myMap = [[[-1] for _ in range(10)] for _ in range(10)]
chargers = []

dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

def makeMap(myMap, chargers):
    n = len(chargers)
    for i in range(n):
        y, x, c, _ =  chargers[i]
        for row in range(max(0, y-c), min(y+c+1, 10)):
            arange = min(row - (y-c), (y+c) - row)
            for j in range(arange+1):
                if j == 0:
                    if myMap[row][x][0] == -1:
                        myMap[row][x] = [i]
                    else:
                        myMap[row][x].append(i)
                else:
                    if myMap[row][max(0, x-j)][0] == -1:
                        myMap[row][max(0, x-j)] = [i]
                    else:
                        myMap[row][max(0, x-j)].append(i)

                    if myMap[row][min(9, x+j)][0] == -1:
                        myMap[row][min(9, x+j)] = [i]
                    else:
                        myMap[row][min(9, x+j)].append(i)
    return

def getScore(myMap, next_a, next_b, chargers):
    y_a, x_a = next_a
    y_b, x_b = next_b
    max_score = -1

    case_a = myMap[y_a][x_a]
    case_b = myMap[y_b][x_b]
    for a in case_a:
        for b in case_b:
            if a == -1:
                score_a = 0
                if b == -1:
                    score_b = 0
                else:
                    score_b = chargers[b][3]

            else:
                if b == -1:
                    score_a = chargers[a][3]
                    score_b = 0
                else:
                    if a == b:
                        score_a = chargers[a][3]//2
                        score_b = chargers[b][3]//2
                    else:
                        score_a = chargers[a][3]
                        score_b = chargers[b][3]

            temp = score_a + score_b

            if temp > max_score:
                max_score = temp

    return max_score


def solve(myMap, chargers, M, score, person_a, person_b, path_a, path_b):
    time = 1
    while (time <= M):
        y_a, x_a = person_a
        y_b, x_b = person_b
        next_a = (y_a + dy[path_a[time-1]], x_a + dx[path_a[time-1]])
        next_b = (y_b + dy[path_b[time-1]], x_b + dx[path_b[time-1]])
        score += getScore(myMap, next_a, next_b, chargers)
        person_a = next_a
        person_b = next_b
        time += 1
    return score


def main():
    T = int(input())
    for t in range(T):
        # Initialize
        for i in range(10):
            for j in range(10):
                myMap[i][j] = [-1]
        chargers.clear()

        M, A = (int(x) for x in input().split())
        path_a = [int(x) for x in input().split()]
        path_b = [int(x) for x in input().split()]
        for a in range(A):
            x, y, c, p = (int(x) for x in input().split())
            chargers.append((y-1, x-1, c, p))
        makeMap(myMap, chargers)
        score = getScore(myMap, (0, 0), (9, 9), chargers)
        person_a = (0, 0)
        person_b = (9, 9)
        result = solve(myMap, chargers, M, score, person_a, person_b, path_a, path_b)
        print("#{} {}".format(t+1, result))


if __name__ == "__main__":
    main()