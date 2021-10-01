'''
1. 재생시간만큼 악보를 늘리거나 줄인다.
    - 재생시간을 분단위로 구하는 메소드 필요
    - #이 포함된 경우 유의. 음 단위로 분리.
2. 변환된 악보들끼리 멜로디와 비교한다.
    - 변환된 악보에서 멜로디의 음 개수만큼 뽑았을 때 일치하는지 확인 
3. 일치하는 것들을 재생시간, 인덱스와 함께 리스트에 추가
    - 리스트의 길이가 0이면 (None)을 반환
    - 여러 개면 재생시간이 긴 것을, 재생시간도 같으면 먼저 입력된 음악 제목. (재생시간 내림차순, 인덱스 오름차순.)
'''

def get_play_time(start, end):
    start_h, start_m = map(int, start.split(":"))
    end_h, end_m = map(int, end.split(":"))
    play_time = (end_h*60 + end_m) - (start_h*60 + start_m)
    return play_time

def split_note(music):
    note_list = []
    for x in music:
        if x == "#":
            note_list[-1] = note_list[-1]+"#"
        else:
            note_list.append(x)
    return note_list

def expand_music(note_list, play_time) -> list:
    expanded_music = []
    n = len(note_list)
    if play_time <= n:
        expanded_music = note_list[:play_time]
    else:
        expanded_music = (play_time//n)*note_list + note_list[:play_time%n]
    return expanded_music

def is_involved(music, melody):
    '''
    music = 10
    melody = 3
    012/123/234/345/456/678/789/8910/
    '''
    n = len(melody)
    is_same = False
    for i in range(len(music)-n+1):
        temp = music[i:i+n]
        if temp == melody:
            is_same = True
            break
    return is_same


def solution(m, musicinfos):
    answer = ''
    search_list = []
    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, music = musicinfo.split(",")
        note_list = split_note(music)
        m_note = split_note(m)
        play_time = get_play_time(start, end)
        music_note = expand_music(note_list, play_time)
        if is_involved(music=music_note, melody=m_note):
            search_list.append((title, play_time, idx))

    if len(search_list) == 0:
        answer = "(None)"
    else:
        search_list = sorted(search_list, key= lambda x: (-x[1], x[2]))
        answer = search_list[0][0]
    return answer


examples = [
    {
        "m": "ABCDEFG",
        "musicinfos": ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    },
    {
        "m": "CC#BCC#BCC#BCC#B",
        "musicinfos": ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    },
    {
        "m": "ABC",
        "musicinfos": ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    }
]

for example in examples:
    print(solution(example["m"], example["musicinfos"]))