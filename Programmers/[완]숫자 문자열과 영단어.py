'''
1. 0번 인덱스부터 각 문자가 알파벳인지 숫자인지 구분한다.
2. 알파벳인 경우
    - start_idx가 -1이면 start_idx에 지금 인덱스를 저장한다.
    - start_idx가 -1이 아니면, start_idx에서 지금 인덱스까지의 문자열로 영단어가 되는지 확인한다.
    - 영단어가 되면 해당하는 숫자를 stack에 추가하고 start_idx를 -1로 초기화한다.
3. 숫자인 경우
    - stack에 추가
'''

num_alphabet_dict = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

def solution(s):
    answer = 0
    stack = []
    start_idx = -1
    for i in range(len(s)):
        if s[start_idx:i] in num_alphabet_dict.keys():
            stack.append(num_alphabet_dict[s[start_idx:i]])
            start_idx = -1
        if s[i].isnumeric():
            start_idx = -1
            stack.append(s[i])
        else:
            if start_idx == -1:
                start_idx = i
    if start_idx != -1:
        stack.append(num_alphabet_dict[s[start_idx:]])    
    answer = int("".join(stack))
    return answer


examples = [
    "one4seveneight",
    "23four5six7",
    "2three45sixseven",
    "123",
]

for example in examples:
    print(solution((example)))