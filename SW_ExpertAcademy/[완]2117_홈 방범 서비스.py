from copy import deepcopy
from pprint import pprint

def getHouse(graph, N, y, x, k):
    num = 0 # 집 수
    for i in range(max(0, y-k+1), min(y+k, N)):
        if i == y-k+1 or i == y+k-1:
            num += graph[i][x]
        else:
            j = min(i - (y-k+1), (y+k-1) - i)
            if x-j >= 0:
                num += graph[i][x - j]
            if x + j < N:
                num += graph[i][x + j]
    return num

def getMaxHouse(graph, table, N, M, k):
    max_house = 0   # 좌표 별로 포함하는 가장 많은 집
    cost = k**2 + (k-1)**2
    for i in range(N):
        for j in range(N):
            table[i][j] += getHouse(graph, N, i, j, k)
            if table[i][j]*M >= cost:
                max_house = max(max_house, table[i][j])
    # print(k)
    # pprint(table)
    return max_house

def solve(graph, N, M, max_k, total_house):
    k = 2
    max_house = 1
    table = deepcopy(graph)
    # pprint(table)
    while (k < max_k):
        max_house = max(getMaxHouse(graph, table, N, M, k), max_house)
        if max_house == total_house:
            break
        k += 1
    return max_house


def main():
    T = int(input())
    for t in range(T):
        N, M = (int(x) for x in input().split())
        graph = []
        total_house = 0
        for i in range(N):
            temp = [int(x) for x in input().split()]
            total_house += sum(temp)
            graph.append(temp)
        max_k = 1
        while ( total_house*M > (max_k**2 + (max_k-1)**2)):
            max_k += 1
        result = solve(graph, N, M, max_k, total_house)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()