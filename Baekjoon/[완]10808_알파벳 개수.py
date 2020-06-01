def main():
    string = input()
    table = [0 for _ in range(26)]
    for i in range(len(string)):
        idx = ord(string[i]) - 97
        table[idx] += 1
    print(*table)

if __name__ == "__main__":
    main()