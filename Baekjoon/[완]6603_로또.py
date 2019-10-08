
def solve(result, numbers, k):
    if len(numbers) == k:
        for i in range(k):
            result += numbers[i] + " "
        print(result[:-1])
        return
    else:
        if k == 0:
            print(result[:-1])
            return
        else:
            solve(result + numbers[0] + " ", numbers[1:], k-1)
            solve(result, numbers[1:], k)

def main():
    while(1):
        line = input().split()
        if line == ["0"]:
            break
        else:
            k = int(line[0])
            numbers = line[1:]
            solve("", numbers, 6)
            print()

if __name__ == "__main__":
    main()