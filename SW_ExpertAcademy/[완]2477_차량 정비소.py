import queue
from collections import deque

def solve(a, b, t, N, M, K, A, B):
    wait_a_Q = deque()  # (도착 시간, 고객 번호)
    for i in range(K):
        wait_a_Q.append((t[i], i))

    wait_b_Q = deque()  # (도착 시간, 고객 번호)
    myPQ = queue.PriorityQueue() # (end time, a or b, 고객 번호)
    endPQ = queue.PriorityQueue()   # (end time, 접수 창구 번호, 고객 번호)
    table = [[-1, -1] for _ in range(K)]    # 거쳐간 창구 번호
    a_status = [0 for _ in range(N)]
    b_status = [0 for _ in range(M)]
    result = 0

    time = t[0]
    while (len(wait_a_Q) != 0 or len(wait_b_Q) != 0 or (not myPQ.empty())):
        # 현재 시간에 창구 상담이 종료되는 것이 있는지 확인
        while(not myPQ.empty()):
            end_time, where, customerNum = myPQ.get()
            if end_time == time:
                if where == 'a':
                    idx = table[customerNum][0] # 접수 창고 번호
                    a_status[idx] = 0
                    endPQ.put((end_time, idx, customerNum))
                else:
                    idx = table[customerNum][1]
                    b_status[idx] = 0
                    if idx + 1 == B:
                        if table[customerNum][0] + 1 == A:
                            result += customerNum + 1
            else:
                myPQ.put((end_time, where, customerNum))
                break

        while(not endPQ.empty()):
            end_time, a_num, customerNum = endPQ.get()
            wait_b_Q.append((end_time, customerNum))


        # 접수 창구를 기다리고 있는 고객 중 상담 받을 사람
        temp_num = 0
        while(len(wait_a_Q) != 0):
            flag = True
            if wait_a_Q[0][0] <= time:
                for i in range(temp_num, N):
                    if a_status[i] == 0:
                        a_status[i] = 1
                        dest_time, customerNum = wait_a_Q.popleft()
                        myPQ.put((time + a[i], "a", customerNum))
                        table[customerNum][0] = i
                        temp_num = i+1
                        flag = False
                        break
                if flag:
                    break
            else:
                break

        # 정비 창구를 기다리고 있는 고객 중 상담 받을 사람
        temp_num = 0
        while(len(wait_b_Q) != 0):
            flag = True
            if wait_b_Q[0][0] <= time:
                for i in range(temp_num, M):
                    if b_status[i] == 0:
                        b_status[i] = 1
                        dest_time, customerNum = wait_b_Q.popleft()
                        myPQ.put((time + b[i], "b", customerNum))
                        table[customerNum][1] = i
                        temp_num = i+1
                        flag = False
                        break
                if flag:
                    break
            else:
                break

        time += 1

    if result == 0:
        result = -1
    return result

def main():
    T = int(input())
    for i in range(T):
        # N : 접수창구 수, M : 정비창구 수, K : 고객 수
        # A : 이용한 접수창구 번호, B : 이용한 정비창구 번호
        N, M, K, A, B = (int(x) for x in input().split())
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        t = [int(x) for x in input().split()]

        result = solve(a, b, t, N, M, K, A, B)

        print("#{} {}".format(i+1, result))

if __name__ == "__main__":
    main()