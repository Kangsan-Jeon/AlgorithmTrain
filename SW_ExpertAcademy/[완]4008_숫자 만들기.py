'''
Algorithm
[브루트포스]
1. 가능한 모든 연산의 경우의 수를 makeCase를 통해 반환한다.
=> 중복이 포함될 수 있으므로 set함수를 사용해 중복을 제거한다.
2. 연산의 경우의 수에 대하여 연산한 결과의 최대값과 최소값을 갱신한다.
=> / 연산을 처음에 //로 적용했지만 1번 테스트 케이스에서 틀린 답이 나오므로 int(num1/num2)로 적용한다.
'''
operator = ["+", "-", "*", "/"]

def makeCase(myOperator):
    cases = [(myOperator[0])]
    for i in range(1, len(myOperator)):
        new_cases = []
        while cases:
            temp = list(cases.pop())
            oper = [myOperator[i]]
            for i in range(len(temp)+1):
                new_case = temp[:i] + oper + temp[i:]
                new_cases.append(new_case)
        cases = list(set(map(tuple, new_cases)))
    return cases

def calculate(num1, num2, oper):
    if oper == "+":
        return num1 + num2
    elif oper == "-":
        return num1 - num2
    elif oper == "*":
        return num1*num2
    else:
        return int(num1/num2)

def solve(myNumber, myOperator, N):
    myMin = 100000001
    myMax = -100000001
    cases = makeCase(myOperator)
    for case in cases:
        num = myNumber[0]
        for i in range(1, N):
            num = calculate(num, myNumber[i], case[i-1])
        myMin = min(myMin, num)
        myMax = max(myMax, num)
    return myMax - myMin

def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        temp_oper = [int(x) for x in input().split()]
        myOperator = []
        for i in range(4):
            for j in range(temp_oper[i]):
                myOperator.append(operator[i])
        myNumber = [int(x) for x in input().split()]
        result = solve(myNumber, myOperator, N)
        print("#{} {}".format(t+1, result))

if __name__ == "__main__":
    main()