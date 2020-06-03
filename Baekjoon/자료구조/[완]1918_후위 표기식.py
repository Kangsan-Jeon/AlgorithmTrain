import sys

priority = {"*": 1, "/": 1, "+": 0, "-": 0, "(": -1}


def change_exp(expression):
    stack = []
    answer = ""
    for x in expression:
        if "A" <= x <= "Z":
            answer += x
        elif x in ["+", "-", "*", "/"]:
            if len(stack) == 0:
                stack.append(x)
            else:
                if priority[stack[-1]] >= priority[x]:  # 이전의 연산자가 우선순위가 더 높거나 같을 때
                    # 지금의 연산자보다 우선순위가 낮을 때 까지 pop
                    while priority[stack[-1]] >= priority[x]:
                        answer += stack.pop()
                        if len(stack) == 0:
                            break
                stack.append(x)
        elif x == "(":
            stack.append(x)
        else:   # 닫힌 괄호
            temp = stack.pop()
            while temp != "(":
                answer += temp
                temp = stack.pop()
    while len(stack) != 0:
        answer += stack.pop()
    return answer


def main():
    expression = sys.stdin.readline().rstrip()
    print(change_exp(expression))


if __name__ == "__main__":
    main()