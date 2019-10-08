from copy import deepcopy

def solve(film, D, W, K):
    num = 0
    while(1):
        if num == 0:
            if checkFilm(film, D, W, K):
                break
            else:
                continue
        num += 1
    return num


def main():
    T = int(input())
    for t in range(T):
        D, W, K = (int(x) for x in input().split())
        film = []
        for d in range(D):
            temp = [int(x) for x in input().split()]
            film.append(temp)
        result = solve(film, D, W, K)
        print("#{} {}".format(t+1, result))


if __name__ == "__main__":
    main()