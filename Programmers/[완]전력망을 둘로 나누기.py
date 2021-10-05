'''
1. 간선 중에 하나를 선택하여 제거한다.
2. 각 전력망 네트워크의 송전탑 개수를 비교한다.
    - 트리 형태에서 하나만 끊기 때문에 한 네트워크의 송전탑 개수 m을 구하면 다른 네트워크의 송전탑 개수는 (n-m)
3. 한 네트워크의 송전탑 개수가 n//2일 때는 break
    - 아니면 제거하지 않은 간선 중 하나에 대해서 1번부터 반복
'''

def get_number_of_tower(graph, visited, v1):
    stack = [v1]
    while len(stack) > 0:
        vertex = stack.pop() - 1
        if visited[vertex]:
            continue
        else:
            visited[vertex] = True
            for i in range(len(graph)):
                if graph[vertex][i] == 1 and visited[i] is False:
                    stack.append(i+1)
    return sum(visited)
                    
def solution(n, wires):
    m = 0
    gap = n
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for wire in wires:
        graph[wire[0]-1][wire[1]-1] = 1
        graph[wire[1]-1][wire[0]-1] = 1

    while len(wires) > 0:
        v1, v2 = wires.pop()
        visited = [False for _ in range(n)]

        # 간선 제거
        graph[v1-1][v2-1] = 0
        graph[v2-1][v1-1] = 0
        m = get_number_of_tower(graph, visited, v1)
        
        # 간선 원복
        graph[v1-1][v2-1] = 1
        graph[v2-1][v1-1] = 1
        
        gap = min(abs(n-2*m), gap)
        if gap == 0 or gap == 1:
            break
    return gap

examples = [
    {
        "n": 9,
        "wires": [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]],
    },
    {
        "n": 4,
        "wires": [[1,2],[2,3],[3,4]],
    },
    {
        "n": 7,
        "wires": [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]],
    },
]

for example in examples:
    print(solution(example['n'], example['wires']))