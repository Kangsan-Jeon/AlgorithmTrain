from sys import stdin
from itertools import combinations

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def is_evitable(graph, teachers):
    N = len(graph)
    for idx in range(len(teachers)):
        i, j = teachers[idx]

        # Check right
        next_j = j + dx[0]
        while (next_j < N):
            if graph[i][next_j] == "O" or graph[i][next_j] == "T":
                break
            elif graph[i][next_j] == "S":
                return False
            next_j += dx[0]
    
        # Check left
        next_j = j + dx[1]
        while (next_j >= 0):
            if graph[i][next_j] == "O" or graph[i][next_j] == "T":
                break
            elif graph[i][next_j] == "S":
                return False
            next_j += dx[1]

        # Check up
        next_i = i + dy[2]
        while (next_i >= 0):
            if graph[next_i][j] == "O" or graph[next_i][j] == "T":
                break
            elif graph[next_i][j] == "S":
                return False
            next_i += dy[2]

        # Check down
        next_i = i + dy[3]
        while (next_i < N):
            if graph[next_i][j] == "O" or graph[next_i][j] == "T":
                break
            elif graph[next_i][j] == "S":
                return False
            next_i += dy[3]
    return True


def main():
    N = int(stdin.readline())
    graph = [stdin.readline().rstrip().split() for _ in range(N)]

    possible_nodes = []
    teachers = []

    for i in range(N):
        for j in range(N):
            if graph[i][j] == "T":
                teachers.append((i, j))
            elif graph[i][j] == "X":
                possible_nodes.append((i, j))
    
    stack = list(combinations(possible_nodes, 3))

    while (len(stack) > 0):
        node_1, node_2, node_3 = stack.pop()
        graph[node_1[0]][node_1[1]] = "O"
        graph[node_2[0]][node_2[1]] = "O"
        graph[node_3[0]][node_3[1]] = "O"
        if is_evitable(graph, teachers):
            return print("YES")
        graph[node_1[0]][node_1[1]] = "X"
        graph[node_2[0]][node_2[1]] = "X"
        graph[node_3[0]][node_3[1]] = "X"
    return print("NO")


if __name__ == "__main__":
    main()