from collections import deque

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, 2, -2, 1, -1]

def solve(my_map, visited, N, start, end):
    myQ = deque()
    myQ.append(start)
    while (len(myQ) != 0):
        y, x = myQ.popleft()
        if my_map[y][x] == 1:
            break
        for i in range(8):
            new_y = y + dy[i]
            new_x = x + dx[i]
            if new_x >= 0 and new_x < N and new_y >= 0 and new_y < N:
                if visited[new_y][new_x] == -1:
                    visited[new_y][new_x] = visited[y][x] + 1
                    myQ.append((new_y, new_x))
    return visited[end[0]][end[1]]

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        start_y, start_x = (int(x) for x in input().split())
        end_y, end_x = (int(x) for x in input().split())
        my_map = [[0 for _ in range(N)] for _ in range(N)]
        visited = [[-1 for _ in range(N)] for _ in range(N)]
        visited[start_y][start_x] = 0
        my_map[end_y][end_x] = 1
        start = (start_y, start_x)
        end = (end_y, end_x)
        result = solve(my_map, visited, N, start, end)
        print(result)

if __name__ == "__main__":
    main()