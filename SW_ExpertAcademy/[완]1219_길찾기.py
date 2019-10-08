def solve(arr1, arr2):
    path = [0]
    while (len(path) != 0):
        temp = path.pop()
        if arr1[temp] == -1 or arr1[temp] == 100:
            continue
        else:
            if arr1[temp] == 99:
                return True
            path.append(arr1[temp])
            if arr2[temp] == 99:
                return True
            elif (arr2[temp] != -1 and arr2[temp] != 100):
                path.append(arr2[temp])
            arr1[temp] = 100
            arr2[temp] = 100
    return False

if __name__ == "__main__":
    for i in range(10):
        t, N = (int(i) for i in input().split())
        arr1 = [-1 for i in range(100)]
        arr2 = [-1 for i in range(100)]
        line = [int(i) for i in input().split()]
        path = []
        for i in range(N):
            start = line[2*i]
            end = line[2*i + 1]
            if arr1[start] == -1:
                arr1[start] = end
            else:
                arr2[start] = end
        if solve(arr1, arr2):
            print("#{} {}".format(t, 1))
        else:
            print("#{} {}".format(t, 0))
