'''
1. dfs를 통해 비어있는 구역과 퍼즐조각 구역을 뽑는다(get_sectors)
2. 비어있는 구역과 퍼즐을 비교한다.
    - 90도씩 4번을 회전시켜 일치하는지 확인
    - 퍼즐조각을 평행이동했을 때 비어있는 구역과 일치 여부 판단
        ㄴ 일치여부 로직
        1) 퍼즐조각 중 한 좌표(코드에서는 0번 인덱스)를 비어있는 구역 중 한 좌표로 옮겨진다고 가정한다.
        2) 만약 퍼즐조각과 비어있는 구역이 일치한다면, 위 좌표의 차이만큼 남은 퍼즐 좌표를 모두 옮겼을 때,
        그 좌표들이 비어있는 구역의 좌표와 같다.
        3) 일치하지 않으면 비어있는 구역 중 다른 좌표를 퍼즐조각 중 한 좌표(0번 인덱스)라고 가정하고 위의 로직을 반복한다.
    - 일치한다면 퍼즐 조각들을 모은 리스트에서 제거하고 퍼즐조각의 칸만큼 더해준다.
    - 불일치 한다면 다른 퍼즐 조각과 비교한다.
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rotate(pices, n):
    '''
    (0, :) -> (:, n-0-1)
    '''
    rotated_piece = []
    for cell in pices:
        y, x = cell
        rotated_y = x
        rotated_x = n-y-1
        rotated_piece.append((rotated_y, rotated_x))
    return rotated_piece

def dfs(array, is_visit, r, c, flag):
    sector = []
    stack = [(r, c)]
    while len(stack) > 0:
        y, x = stack.pop()
        if not is_visit[y][x]:
            is_visit[y][x] = True
            sector.append((y, x))
            for  i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if (0 <= new_x < len(array)) and (0 <= new_y < len(array)):
                    if (is_visit[new_y][new_x] is False) and (array[new_y][new_x] == flag):
                        stack.append((new_y, new_x))
    return sector

def get_sectors(array, flag):
    blank_sectors = []
    is_visit = [[False for _ in range(len(array))] for _ in range(len(array))]
    for r in range(len(array)):
        for c in range(len(array)):
            if array[r][c] == int(not bool(flag)):
                is_visit[r][c] = True
            else:
                if is_visit[r][c] is False:
                    blank_sectors.append(dfs(array, is_visit, r, c, flag))
    return blank_sectors

def is_match(sector, piece, n):
    answer = False
    origin_piece = [x for x in piece]
    if len(sector) != len(piece):
        pass
    else:
        for _ in range(4):
            flag = True
            piece = rotate(piece, n)
            for i in range(len(sector)):
                flag = True
                sector_y, sector_x = sector[i]
                diff_y = sector_y - piece[0][0]
                diff_x = sector_x - piece[0][1]
                for piece_y, piece_x in piece:
                    if (piece_y + diff_y, piece_x + diff_x) in sector:
                        pass
                    else:
                        flag = False
                        break
                if flag:
                    answer = True
                    break
            if answer:
                print(f"Blank Sector: {sector}")
                print(f"Piece: {origin_piece}")
                break
    return answer

def solution(game_board, table):
    answer = 0
    blank_sectors = get_sectors(game_board, flag=0)
    pieces = get_sectors(table, flag=1)
    print(f"Blank Sectors: {blank_sectors}")
    print(f"Pieces: {pieces}")
    for sector in blank_sectors:
        for i in range(len(pieces)):
            piece = pieces[i]
            if is_match(sector, piece, len(game_board)):
                answer += len(piece)
                pieces.remove(piece)
                break
    return answer

examples = [
    {
        'game_board': [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
        'table': [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]],
    },
    {
        'game_board': [[0,0,0],[1,1,0],[1,1,1]],
        'table': [[1,1,1],[1,0,0],[0,0,0]],
    },
    {
        'game_board': [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
        'table': [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,0,1],[0,1,0,0,1,1]],
    },
    {
        'game_board': [[0]],
        'table': [[1]],
    },
    {
        'game_board': [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]],
        'table': [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]],
    },
]


for example in examples[-1:]:
    print(solution(example['game_board'], example['table']))