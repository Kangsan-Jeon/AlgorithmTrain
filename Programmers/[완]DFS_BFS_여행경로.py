def DFS(tickets, visited, start):
    result = [start]
    n = len(tickets)

    for i in range(n):
        if tickets[i][0] == start and visited[i] == False:
            visited[i] = True
            result = result + DFS(tickets, visited, tickets[i][1])
            if False in visited:
                result = [start]
                visited[i] = False
    return result

def solution(tickets):
    n = len(tickets)
    visited = [False for i in range(n)]

    tickets.sort(key=lambda x: x[1])

    answer = DFS(tickets, visited, "ICN")
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

print(solution([["ICN", "SFO"], ["ICN", "ATL"],
                ["SFO", "ATL"], ["SFO", "ICN"],
                ["ATL", "SFO"]]))

print(solution([["ICN", "SFO"], ["ICN", "ATL"],
                ["SFO", "ATL"], ["ATL", "ICN"],
                ["ATL", "SFO"]]))