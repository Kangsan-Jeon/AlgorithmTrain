'''
1. 0번 인덱스를 prev_char에 저장하고 stack에는 짝지어지지 못한 문자들을 저장한다.
2. prev_char과 현재의 문자를 비교한다
    - 같은 경우
        ㄴ 짝지어졌으므로 stack에서 하나 pop
        ㄴ 만약 stack이 비어있으면, prev_char에는 빈 문자열을 저장한다.
        ㄴ stack이 비어있지 않으면, prev_char로 stack의 마지막 문자를 지정한다.
    - 다른 경우(prev_char이 비어있는 경우 포함)
        ㄴ prev_char에 지금 인덱스의 문자를 저장한다.
        ㄴ stack에 지금 인덱스의 문자를를 추가한다.
3. 한 번 돌았을 때 stack이 비어있으면 1을, 그렇지 않으면 0을 반환한다.
'''

def solution(s):
    answer = 0
    prev_char = s[0]
    idx = 1
    stack = [prev_char]

    while (idx < len(s)):
        if prev_char == s[idx]:
            stack.pop()
            if len(stack) > 0:
                prev_char = stack[-1]
            else:
                prev_char = ""
        else:
            prev_char = s[idx]
            stack.append(prev_char)
        idx += 1
    if len(stack) == 0:
        answer = 1
    return answer


examples = [
    "baabaa",
    "cdc"
]

for example in examples:
    print(solution(example))