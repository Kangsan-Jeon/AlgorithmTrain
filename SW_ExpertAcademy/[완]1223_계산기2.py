
def mul(lst):
    new_lst = []
    n = len(lst)
    ind = 0
    while (ind < n):
        temp = lst[ind]
        if temp == "*":
            oper1 = new_lst.pop()
            new_lst.append(oper1 + lst[ind+1] + temp)
            ind += 2
        else:
            new_lst.append(temp)
            ind += 1
    return new_lst

def plus(lst):
    new_lst = []
    n = len(lst)
    ind = 0
    while (ind < n):
        temp = line[ind]
        if temp == "+":
            oper1 = new_lst.pop()
            new_lst.append(oper1 + lst[ind+1] + temp)
            ind += 2
        else:
            new_lst.append(temp)
            ind += 1
    return new_lst

if __name__ == "__main__":
    for t in range(10):
        l = int(input())
        line = input()
        if line.find('*') != -1:
            line = list(line)
            line = mul(line)
            line = plus(line)
        else:
            line = plus(line)

        ind = 0
        line = list(line[0])
        while(len(line) != 1):
            temp = line[ind]
            if temp == "+" or temp == "*":
                oper1 = int(line.pop(ind-2))
                oper2 = int(line.pop(ind-2))
                operator = line.pop(ind-2)
                if operator == "+":
                    line.insert(ind-2, str(oper1 + oper2))
                else:
                    line.insert(ind - 2, str(oper1 * oper2))
                ind = ind-1
            else:
                ind+=1
        print("#{} {}".format(t+1, line[0]))
