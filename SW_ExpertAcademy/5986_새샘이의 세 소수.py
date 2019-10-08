T = int(input())


# Make list of boxes
for i in range(T):
    N = int(input())
    lst = []
    for j in range(N):
        x = int(input())
        lst.append(x)
    lst.sort()
    print("#{} {}".format(i+1, cal(lst)))