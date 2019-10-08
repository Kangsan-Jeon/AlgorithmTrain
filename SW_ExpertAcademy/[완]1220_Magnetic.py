

if __name__ == "__main__":
    for t in range(10):
        n = int(input())
        arr = []
        cnt = 0
        for i in range(n):
            line = [int(x) for x in input().split()]
            arr.append(line)

        for col in range(n):
            flag = False
            for row in range(n):
                if arr[row][col] == 1:
                    flag = True
                elif (flag and arr[row][col] == 2):
                    cnt += 1
                    flag = False


        print("#{} {}".format(t+1, cnt))
