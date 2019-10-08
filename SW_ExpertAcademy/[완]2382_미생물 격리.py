import queue

def countNum(graph):
    N = len(graph)
    cnt = 0
    for i in range(N):
        for j in range(N):
            cnt += graph[i][j][0]
    return cnt


def getNext(graph, y, x, n, direction):
    N = len(graph)
    if direction == 1:
        next_x = x
        next_y = y-1
        next_n = n
        next_direction = direction
        if next_y == 0:
            next_direction = 2
            next_n = n//2

    elif direction == 2:
        next_x = x
        next_y = y+1
        next_n = n
        next_direction = direction
        if next_y == N - 1:
            next_direction = 1
            next_n = n//2

    elif direction == 3:
        next_x = x - 1
        next_y = y
        next_n = n
        next_direction = direction
        if next_x == 0:
            next_direction = 4
            next_n = n//2

    else:
        next_x = x + 1
        next_y = y
        next_n = n
        next_direction = direction
        if next_x == N - 1:
            next_direction = 3
            next_n = n//2

    if next_n == 0:
        return None
    else:
        return (next_y, next_x, next_n, next_direction)

def solve(graph, M, que):
    newQ = queue.Queue()
    next_list = []
    if M == 0:
        return countNum(graph)
    else:
        while(not que.empty()):
            y, x = que.get()
            n, direction = graph[y][x]
            temp = getNext(graph, y, x, n, direction)
            # print(temp)
            graph[y][x] = [0, 0]
            if temp is None:
                continue
            else:
                next_list.append(temp)

        next_list.sort(key=lambda x:x[2], reverse=True)
        # print(next_list)

        for i in range(len(next_list)):
            temp_y, temp_x, temp_n, temp_dir = next_list[i]
            if graph[temp_y][temp_x][0] > 0:
                graph[temp_y][temp_x][0] += temp_n
            else:
                graph[temp_y][temp_x] = [temp_n, temp_dir]
                newQ.put((temp_y, temp_x))

        # pprint(graph)
        return solve(graph, M-1, newQ)

def main():
    T = int(input())
    for t in range(T):
        N, M, K = (int(x) for x in input().split())
        graph = [[[0, 0] for _ in range(N)] for _ in range(N)]

        myQ = queue.Queue()
        for k in range(K):
            y, x, n, direction = (int(x) for x in input().split())
            graph[y][x] = [n, direction]
            myQ.put((y, x))

        result = solve(graph, M, myQ)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()