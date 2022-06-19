def solution(src, dest, debug=False):

    chess_board = [0 for _ in range(64)]
    moves = [-15, -13, -9, -5, 5, 9, 13, 15]

    # Mark the src as visited, and add it to the queue
    chess_board[src] = 1
    Q = [(src, 0)]

    while Q:
        if debug:
            print(Q)
        current_position, path_length = Q.pop(0)

        if current_position == dest:
            return path_length

        for m in moves:

            position = current_position + m

            if legal_move(current_position, position) and chess_board[position] != 1:
                # mark as visited and add to queue
                chess_board[position] = 1
                Q.append((position, path_length + 1))


def legal_move(src, dst, number_of_squares=64):
    if not (-1 < dst and dst < number_of_squares):
        return False

    x1 = src // 8
    y1 = src % 8
    x2 = dst // 8
    y2 = dst % 8
    return diff(x1, x2) <= 2 or diff(y1, y2) <= 2


def diff(a, b):
    if a > b:
        return a - b
    return b - a


from collections import defaultdict


def alt_solution(src, dst):

    DIMENSIONS = 8
    src_row = src // DIMENSIONS
    src_col = src % DIMENSIONS

    dst_row = dst // DIMENSIONS
    dst_col = dst % DIMENSIONS
    dst_tpl = dst_row, dst_col

    board = [[0 for _ in range(DIMENSIONS)] for _ in range(DIMENSIONS)]
    visited = defaultdict(lambda: False)

    Q = [(src_row, src_col, 0)]
    visited[(src_row, src_col)] = True
    while Q:
        current_row, current_col, depth = Q.pop(0)
        current_tpl = current_row, current_col

        if current_tpl == dst_tpl:
            return depth

        moves = get_moves(current_row, current_col)
        for move in moves:
            if not visited[move]:
                visited[move] = True
                row, col = move
                Q.append((row, col, depth + 1))


def get_moves(row, col):
    moves = [
        (row - 1, col - 2),
        (row - 1, col + 2),
        (row + 1, col - 2),
        (row + 1, col + 2),
        (row - 2, col - 1),
        (row - 2, col + 1),
        (row + 2, col - 1),
        (row + 2, col + 1),
    ]

    return [(x, y) for (x, y) in moves if x > -1 and x < 8 and y > -1 and y < 8]


for i in range(64):
    for j in range(64):
        try:
            assert solution(i, j) == alt_solution(i, j)
        except:
            print("I :", i, "J :", j)
            print(solution(i, j, True), alt_solution(i, j))
            exit()


#            0  1  2  3  4  5  7
#           8  9 10 11 12 13 14
#         15 16 17 18 19 20 21
