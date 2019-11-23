def solution(phone_book):
    table = [[] for _ in range(20)]
    phone_book.sort(key=lambda x: len(x))
    for number in phone_book:
        n = len(number)
        if table[n-1].count(number) != 0:
            return False
        else:
            table[n-1].append(number)
            while (n > 1):
                number = number[:-1]
                n -= 1
                if table[n-1].count(number) != 0:
                    return False
    return True