
'''
복서 선수들의 몸무게 weights와, 복서 선수들의 전적을 나타내는 head2head가 매개변수로 주어집니다.
복서 선수들의 번호를 다음과 같은 순서로 정렬한 후 return 하도록 solution 함수를 완성해주세요.
    1. 전체 승률이 높은 복서의 번호가 앞쪽으로 갑니다. 아직 다른 복서랑 붙어본 적이 없는 복서의 승률은 0%로 취급합니다.
    2. 승률이 동일한 복서의 번호들 중에서는 자신보다 몸무게가 무거운 복서를 이긴 횟수가 많은 복서의 번호가 앞쪽으로 갑니다.
    3. 자신보다 무거운 복서를 이긴 횟수까지 동일한 복서의 번호들 중에서는 자기 몸무게가 무거운 복서의 번호가 앞쪽으로 갑니다.
    4. 자기 몸무게까지 동일한 복서의 번호들 중에서는 작은 번호가 앞쪽으로 갑니다.
'''

def get_win_info(idx, weights, record):
    w_cnt = 0
    w_heavier_cnt = 0
    n_cnt = 0
    for i in range(len(record)):
        if record[i] == "W":
            w_cnt += 1
            if weights[i] > weights[idx]:
                w_heavier_cnt += 1
        elif record[i] == 'N':
            n_cnt += 1
    try:
        win_rate = w_cnt/(len(record)-n_cnt)
    except ZeroDivisionError:
        win_rate = 0.
    return (win_rate, w_heavier_cnt)


def solution(weights, head2head):
    num_boxer = len(weights)
    boxer_info = [
        [0., 0, weights[i], i] for i in range(num_boxer)    # [승률, 무거운 복서 이긴 횟수, 몸무게, 번호]
    ]

    for i in range(num_boxer):
        boxer_info[i][0], boxer_info[i][1] = get_win_info(i, weights, head2head[i])

    boxer_info = sorted(boxer_info, key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    # print(boxer_info)
    answer = [value[3]+1 for value in boxer_info]
    return answer


examples = [
    {
        'weights': [50,82,75,120],
        'head2head': ["NLWL","WNLL","LWNW","WWLN"]
    },
    {
        'weights': [145,92,86],
        'head2head': ["NLW","WNL","LWN"]
    },
    {
        'weights': [60,70,60],
        'head2head': ["NNN","NNN","NNN"]
    },    
]

for example in examples:
    print(solution(example['weights'], example['head2head']))