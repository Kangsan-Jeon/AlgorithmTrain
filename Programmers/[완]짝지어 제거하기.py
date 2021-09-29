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