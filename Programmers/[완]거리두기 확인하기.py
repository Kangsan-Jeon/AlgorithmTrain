'''
1. 사람들의 좌표를 뽑는다.
2. 사람들 사이의 맨허튼 거리를 구한다.
    - 맨허튼 거리가 1인 경우, 바로 이어 앉을 때이므로 거리두기를 지키지 않고 있다.
    - 맨허튼 거리가 2인 경우
        ㄴ 두 사람이 같은 행이나 열에 있는 경우, 둘 사이가 파티션이면 거리두기, 그렇지 않으면 거리두기X
        ㄴ 두 사람이 대각선으로 있는 경우, 둘 사이 맨허튼 거리가 1인 좌표가 모두 파티션이면 거리두기, 그렇지 않으면 거리두기X
    - 맨허튼 거리가 2 이상인 경우, 거리두기를 지키고 있다
'''
def get_people(place):
    people = []
    for r in range(len(place)):
        for c in range(len(place)):
            if place[r][c] == "P":
                people.append((r, c)) 
    return people

def check(place):
    people = get_people(place)
    is_right = True
    for i in range(len(people)-1):
        per1_r, per1_c = people[i]
        for j in range(i+1, len(people)):
            per2_r, per2_c = people[j]
            if abs(per1_r - per2_r) + abs(per1_c-per2_c) == 1:
                is_right = False
                break
            elif abs(per1_r - per2_r) + abs(per1_c-per2_c) == 2:
                max_r = max(per1_r, per2_r)
                max_c = max(per1_c, per2_c)
                min_r = min(per1_r, per2_r)
                min_c = min(per1_c, per2_c)
                if min_r == max_r:
                    # 두 사람이 가로로 앉아 있을 때
                    if place[min_r][min_c+1] == "X":
                        pass
                    else:
                        is_right = False
                        break                
                elif min_c == max_c:
                    # 두 사람이 세로로 앉아 있을 때
                    if place[min_r+1][min_c] == "X":
                        pass
                    else:
                        is_right = False
                        break
                else:
                    # 두 사람이 대각선으로 앉아 있을 때
                    if (max_r, max_c) in [people[i], people[j]]:
                        # 두 사람이 2사분면과 4사분면에 있을 때
                        if place[max_r][min_c] == "X" and place[min_r][max_c] == "X": 
                            pass
                        else:
                            is_right = False
                            break
                    else:
                        # 두 사람이 1사분면과 3사분면에 있을 때
                        if place[min_r][min_c] == "X" and place[max_r][max_c] == "X": 
                            pass
                        else:
                            is_right = False
                            break
        if is_right is False:
            break

    return is_right

            
def solution(places):
    answer = []
    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer


examples = [
    [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]],
    [["OPOOO", "PXXOX", "OOXOX", "OOXOX", "OOXXO"], ["XOOOX", "OXXXX", "OXXXO", "OXXXO", "OOOOO"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
]

for example in examples:
    print(solution(example))