if __name__ == "__main__":
    N, K = (int(i) for i in input().split())
    position = [0 for i in range(max(N, K)+2)]  # start = 1, visited = -1, destination = 2
    position[N] = 1
    position[K] = 2
    cnt = [0 for i in range(max(N, K)+2)]
    cnt[N] = 0
    que = [N]
    while (len(que) != 0):
        pos = que.pop(0)
        if position[pos] == -1:
            continue
        elif position[pos] == 2:
            break
        else:
            if pos + 1 < K + 2:
                if cnt[pos + 1] == 0:
                    cnt[pos + 1] = cnt[pos] + 1
                que.append(pos + 1)
            if pos - 1 >= 0:
                if cnt[pos - 1] == 0:
                    cnt[pos - 1] = cnt[pos] + 1
                que.append(pos - 1)
            if 2*pos < K + 2:
                if cnt[pos * 2] == 0:
                    cnt[pos * 2] = cnt[pos] + 1
                que.append(pos * 2)
        position[pos] = -1
    print(cnt[K])