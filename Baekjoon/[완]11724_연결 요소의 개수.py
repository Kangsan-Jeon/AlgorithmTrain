def getParent(parent, node):
    while (parent[node] != node):
        node = parent[node]
    return node


def solve(lines, N, M):
    '''
    :param lines: information of line
    :param N: # of nodes
    :param M: # of line
    :return: # of connected component
    '''

    parent = [i for i in range(N)]
    cnt = 0

    for u, v in lines:
        u = getParent(parent, u)
        v = getParent(parent, v)
        if u != v:
            parent[v] = u
            cnt += 1

    return N-cnt

def main():
    N, M = (int(i) for i in input().split())
    lines = []
    for i in range(M):
        line = (int(x)-1 for x in input().split())
        lines.append(line)
    print(solve(lines, N, M))



if __name__ == "__main__":
    main()