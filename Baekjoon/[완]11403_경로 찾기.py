from collections import deque

def solve(arr, dest, N):
    answer = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dfs = [*dest[i]]
        visited = [0 for i in range(N)]
        while(len(dfs) != 0):
            temp = dfs.pop()
            answer[i][temp] = 1
            if visited[temp] == 0:
                dfs += dest[temp]
                visited[temp] = 1
            else:
                continue

    return answer

def main():
    N = int(input())
    arr = []
    dest = [[] for _ in range(N)]
    for i in range(N):
        inp = input().split()
        temp = []
        for j in range(N):
            if inp[j] == '1':
                dest[i].append(int(j))
            temp.append(int(inp[j]))
        arr.append(temp)

    answer = solve(arr, dest, N)

    for row in answer:
        print(*row)



if __name__ == "__main__":
    main()