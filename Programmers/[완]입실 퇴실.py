def solution(enter, leave):
    '''
    사회적 거리두기를 위해 회의실에 출입할 때 명부에 이름을 적어야 합니다.
    입실과 퇴실이 동시에 이뤄지는 경우는 없으며, 입실 시각과 퇴실 시각은 따로 기록하지 않습니다.
    오늘 회의실에는 총 n명이 입실 후 퇴실했습니다.
    편의상 사람들은 1부터 n까지 번호가 하나씩 붙어있으며, 두 번 이상 회의실에 들어온 사람은 없습니다.
    이때, 각 사람별로 반드시 만난 사람은 몇 명인지 구하려 합니다.
    회의실에 입실한 순서가 담긴 정수 배열 enter, 퇴실한 순서가 담긴 정수 배열 leave가 매개변수로 주어질 때,
    각 사람별로 반드시 만난 사람은 몇 명인지 번호 순서대로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
    '''
    room = []
    meeting_table = [[False for _ in range(len(enter))] for _ in range(len(enter))]

    while len(leave) > 0:
        out_person = leave.pop(0)
        # 나가는 사람이 회의실에 없는 경우 -> 그 사람이 나올 때까지 enter에서 pop
        if out_person not in room:
            in_person = None
            while (in_person != out_person) and (len(enter) != 0):
                in_person = enter.pop(0)
                room.append(in_person)
                if in_person is not None:
                    # 아직 나가지 않은 사람이 들어올 경우 기존에 회의실에 있던 사람과 만난 것을 표시
                    for person in room:
                        if in_person != person:
                            meeting_table[in_person-1][person-1] = True
                            meeting_table[person-1][in_person-1] = True
        room.remove(out_person) # 나가는 사람을 회의실에서 제거
    answer = [sum(x) for x in meeting_table]
    return answer

examples = [
    {
        'enter': [1,3,2],
        'leave': [1,2,3],
    },
    {
        'enter': [1,4,2,3],
        'leave': [2,1,3,4],
    },
        {
        'enter': [3,2,1],
        'leave': [2,1,3],
    },
        {
        'enter': [3,2,1],
        'leave': [1,3,2],
    },
        {
        'enter': [1,4,2,3],
        'leave': [2,1,4,3],
    }, 
]

for example in examples:
    print(solution(example["enter"], example["leave"]))