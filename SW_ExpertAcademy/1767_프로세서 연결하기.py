
def solve(graph, cores):

    return


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        graph = []
        cores = []
        for i in range(N):
            temp = [int(x) for x in input().split()]
            for j in range(N):
                if temp[j] == 1 and i != 0 and i != N-1 and j != 0 and j != N-1:
                    cores.append((i, j))
            graph.append(temp)

        solve(graph, cores)


if __name__ == "__main__":
    main()