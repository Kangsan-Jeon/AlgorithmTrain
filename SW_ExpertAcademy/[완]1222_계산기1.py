import queue

if __name__ == "__main__":
    for t in range(10):
        l = int(input())
        stack = []
        line = input()
        post_trans = []
        ind = 0
        que = queue.Queue()
        while (ind < l):
            if line[ind] == '+':
                post_trans.append(int(line[ind+1]))
                post_trans.append(line[ind])
                ind += 2
            else:
                post_trans.append(int(line[ind]))
                ind += 1
        while (len(post_trans) != 1):
            oper1 = post_trans.pop(0)
            oper2 = post_trans.pop(0)
            operator = post_trans.pop(0)
            temp = oper1 + oper2
            post_trans.insert(0, temp)
        print("#{} {}".format(t+1, post_trans[0]))
