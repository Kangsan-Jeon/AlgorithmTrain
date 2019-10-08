def dfs(plans, values, table, myStack):
    if len(myStack) == 0:
        return table[12]
    else:
        curCost, idx = myStack.pop() # curCost: idx월까지 비용 합, (idx+1)월 확인 필요
        if idx == 12:
            if table[12] > curCost:
                table[12] = curCost
            return dfs(plans, values, table, myStack)
        else:
            # 3 month
            newCost = curCost + values[2]
            if newCost < table[min(idx+3, 12)]:
                myStack.append((newCost, min(idx+3, 12)))
                table[min(idx+3, 12)] = newCost
            # 1 month
            newCost = curCost + values[1]
            if newCost < table[idx+1]:
                myStack.append((newCost, idx+1))
                table[idx+1] = newCost
            # 1 day
            newCost = curCost + values[0]*plans[idx]
            if newCost < table[idx+1]:
                myStack.append((newCost, idx+1))
                table[idx+1] = newCost
            return dfs(plans, values, table, myStack)

def getMinCost(plans, values):
    minCost = values[3]
    table = [minCost for _ in range(13)]
    table[0] = 0
    table[12] = minCost
    idx = 0
    myStack = []
    while (idx < 12):
        if plans[idx] != 0:
            break
        idx += 1

    if minCost > values[2]:
        myStack.append((values[2], idx+3))
        table[idx+3] = values[2]    # idx = 0 -> 1, 2, 3의 합 -> table[3]

    if values[0]*plans[idx] > values[1]:
        myStack.append((values[1], idx + 1))
        table[idx+1] = values[1]
    else:
        myStack.append((values[0]*plans[idx], idx+1))
        table[idx+1] = values[0]*plans[idx]
    return dfs(plans, values, table, myStack)

def main():
    T = int(input())
    for t in range(T):
        values = [int(x) for x in input().split()]
        plans = [int(x) for x in input().split()]

        print("#{} {}".format(t+1, getMinCost(plans, values)))


if __name__ == "__main__":
    main()