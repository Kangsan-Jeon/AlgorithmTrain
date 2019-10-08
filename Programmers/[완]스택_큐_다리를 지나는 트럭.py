import queue

def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    myQueue = queue.Queue()
    cur_weight = 0
    idx = 0
    time = 1
    crossing_end_time = []
    while(idx < n):
        if myQueue.empty():
            myQueue.put((truck_weights[idx], time))
            crossing_end_time.append(time + bridge_length)
            cur_weight += truck_weights[idx]
            idx += 1
        else:
            if crossing_end_time[0] == time:
                crossing_end_time = crossing_end_time[1:]
                crossed_weight, crossed_start_time = myQueue.get()
                cur_weight -= crossed_weight
            if cur_weight + truck_weights[idx] <= weight:
                myQueue.put((truck_weights[idx], time))
                crossing_end_time.append(time + bridge_length)
                cur_weight += truck_weights[idx]
                idx += 1
        time += 1

    while (not myQueue.empty()):
        prev_weight, start_time = myQueue.get()
        time = start_time + bridge_length
    return time

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(2, 4, [1, 2, 1, 2]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,11]))