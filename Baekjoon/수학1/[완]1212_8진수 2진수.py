import sys

to_binary = {"0": "000", "1": "001", "2": "010", "3": "011", "4": "100",
             "5": "101", "6": "110", "7": "111"}


def main():
    octet = sys.stdin.readline().rstrip()
    answer = ""

    for i in range(len(octet)):
        answer += to_binary[octet[i]]

    if answer[0] == "0":
        if answer[1] == "0":
            print(answer[2:])
        else:
            print(answer[1:])
    else:
        print(answer)


if __name__ == "__main__":
    main()
