
def quickSort(values):
    n = len(values)
    if n == 0:
        return []
    elif n == 1:
        return [values[0]]
    pivot = values[0]
    smallerValues = []
    biggerValues = []
    for i in range(1, n):
        if values[i] <= pivot:
            smallerValues.append(values[i])
        else:
            biggerValues.append(values[i])

    return quickSort(smallerValues) + [pivot] + quickSort(biggerValues)


match = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5,
         "SIX":6, "SVN":7, "EGT":8, "NIN":9}


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        test_num, l = (x for x in input().split())
        l = int(l)
        line = [match[x] for x in input().split()]
        sorted_list = quickSort(line)
        key_list = list(match.keys())
        converted_list = [key_list[x] for x in sorted_list]
        print(test_num)
        for x in converted_list:
            print(x, end=" ")
        print()

