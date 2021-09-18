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