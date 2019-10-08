import copy
import queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve(graph, virus, n_safe_area):
    row = len(graph)
    col = len(graph[0])
    n_virus = 0
    while(len(virus) != 0):
        y, x = virus.pop()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x and next_x < col and 0 <= next_y and next_y < row:
                if graph[next_y][next_x] == 0:
                    graph[next_y][next_x] = 2
                    virus.append((next_y, next_x))
                    n_virus += 1
    return n_safe_area - n_virus


def main():
    row, col = (int(x) for x in input().split())
    graph = []
    safe_area = []
    virus = []
    for i in range(row):
        temp = [int(x) for x in input().split()]
        for j in range(col):
            if temp[j] == 0:
                safe_area.append((i, j))
            elif temp[j] == 2:
                virus.append((i, j))
        graph.append(temp)

    n_safe_area = len(safe_area)
    result = 0
    for i in range(n_safe_area-2):
        i_row, i_col = safe_area[i]
        for j in range(i+1, n_safe_area-1):
            j_row, j_col = safe_area[j]
            for k in range(j+1, n_safe_area):
                k_row, k_col = safe_area[k]
                copy_graph = copy.deepcopy(graph)
                copy_virus = copy.deepcopy(virus)
                copy_graph[i_row][i_col] = 1
                copy_graph[j_row][j_col] = 1
                copy_graph[k_row][k_col] = 1
                result = max(solve(copy_graph, copy_virus, n_safe_area - 3), result)

    print(result)

if __name__ == "__main__":
    main()