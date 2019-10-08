def solution(n, computers):
    answer = 0
    dfs = []
    visited = [False for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == False:
                answer += 1
                computers[i][j] = 2
                computers[j][i] = 2
                visited[j] = True
                dfs.append(j)
                while(len(dfs) != 0):
                    node = dfs.pop()
                    for k in range(n):
                        if computers[node][k] == 1 and visited[k] == False:
                            computers[node][k] = 2
                            computers[node][k] = 2
                            visited[k] = 2
                            dfs.append(k)

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))