from copy import deepcopy

'''
Algorithm
1. 현재 map 상에 전체 집 수에 대해서 최대가 될 수 있는 k의 값을 max_k에 저장한다
(Ex. 집이 총 14채이고 M = 3일 때 최대 수익은 42이므로 k=6(비용은 61)일 때부터는 모든 집을 포함해도 손해가 발생한다)
2. table이라는 배열에 k일 때 포함되는 집 수를 저장한다
3. k가 증가할 때 추가되는 영역에 대해서 새로 포함되는 집 수를 getHouse를 통해 반환한다.
4. 만약 손해가 발생하지 않고 기존의 max_house보다 크면 max_house를 갱신한다.
5. k일 때 최대 집 수를 getMaxHouse를 통해 반환한다.
6. 모든 k에 대해서 최대 집 수를 solve를 통해 반환한다.
'''

def getHouse(graph, N, y, x, k):
    '''
    :param graph: map
    :param N: map의 크기
    :param y: 방범 영역의 중심의 y좌표
    :param x: 방범 영역의 중심의 x좌표
    :param k: 방범 구역의 크기
    :return: 현재 위치에서 방범 구역이 (k-1)에서 k로 증가했을 때 추가되는 집의 수
    '''
    num = 0     # 집 수
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
    '''
    :param graph: map
    :param table: 각 좌표에서 방범 크기가 (k-1)일 때 포함되는 집의 수
    :param N: map의 크기
    :param M: 한 집당 발생하는 수익
    :param k: 방범 구역의 크기
    :return: 방범 구역의 크기가 k일 때 가장 많은 서비스를 제공할 수 있는 집의 수
    '''
    max_house = 0   # 좌표 별로 포함하는 가장 많은 집
    cost = k**2 + (k-1)**2
    for i in range(N):
        for j in range(N):
            table[i][j] += getHouse(graph, N, i, j, k)
            if table[i][j]*M >= cost:   # 손해가 발생하지 않는 경우에만 max_house를 갱신
                max_house = max(max_house, table[i][j])
    return max_house

def solve(graph, N, M, max_k, total_house):
    '''
    :param graph: map
    :param N: map의 크기
    :param M: 한 집당 발생하는 수익
    :param max_k: 가능한 k의 maximum + 1의 값
    :param total_house: map상의 전체 집 수
    :return: 가능한 k에 대하여 가장 많은 서비스를 제공할 수 있는 집의 수
    '''
    k = 2
    max_house = 1
    table = deepcopy(graph)
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