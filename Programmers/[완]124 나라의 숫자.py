'''
1. 124 나라는 3진법을 사용하지만 자리수가 0, 1, 2로 이루어지지 않고 1, 2, 3으로 이루어져있다.
    - 따라서 3으로 나누었을 때 몫이 n이고 나머지가 0인 경우, 124 나라에서는 몫이 n-1이고 나머지는 3이다.
    Ex) 21: (기존) (3*2+1)*3 + 0 -> 210, (124 나라) (3*2+0)*3 + 3 ->203
2. 위의 사항만 고려하여 3진법으로 변환한다.
'''

def convert(n):
    result = ""
    mapping_dict = {
        0: "4",
        1: "1",
        2: "2"
    }
    while(n > 0):
        rem = n%3
        n = n//3
        result = mapping_dict[rem] + result
        n = n-1 if rem == 0 else n
    return result

def solution(n):
    answer = convert(n)
    return answer

examples = [1, 2, 3, 4]

for example in examples:
    print(solution(example))