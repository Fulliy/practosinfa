import random

def find_winning_move(board, symbol):
    """
    Ищет ход, который позволит symbol выиграть или заблокировать победу оппонента.
    Возвращает (row, col) если найден выигрышный ход, иначе (-1, -1).
    """
    board_size = len(board)

    # Проверка строк
    for r in range(board_size):
        count = 0
        empty_col = -1
        for c in range(board_size):
            if board[r][c] == symbol:
                count += 1
            elif board[r][c] == '.':
                empty_col = c
            else: # Ячейка занята оппонентом
                count = -1 # Исключаем эту строку как потенциально выигрышную/блокирующую
                break
        if count == board_size - 1 and empty_col != -1:
            return (r, empty_col)

    # Проверка столбцов
    for c in range(board_size):
        count = 0
        empty_row = -1
        for r in range(board_size):
            if board[r][c] == symbol:
                count += 1
            elif board[r][c] == '.':
                empty_row = r
            else:
                count = -1
                break
        if count == board_size - 1 and empty_row != -1:
            return (empty_row, c)

    # Проверка главной диагонали
    count = 0
    empty_r, empty_c = -1, -1
    for i in range(board_size):
        if board[i][i] == symbol:
            count += 1
        elif board[i][i] == '.':
            empty_r, empty_c = i, i
        else:
            count = -1
            break
    if count == board_size - 1 and empty_r != -1:
        return (empty_r, empty_c)

    # Проверка побочной диагонали
    count = 0
    empty_r, empty_c = -1, -1
    for i in range(board_size):
        if board[i][board_size - 1 - i] == symbol:
            count += 1
        elif board[i][board_size - 1 - i] == '.':
            empty_r, empty_c = i, board_size - 1 - i
        else:
            count = -1
            break
    if count == board_size - 1 and empty_r != -1:
        return (empty_r, empty_c)

    return (-1, -1) # Нет выигрышного хода

def get_bot_move(board, bot_symbol):
    """
    Вычисляет оптимальный ход для бота.
    Реализует стратегию: выигрыш -> блокировка -> центр -> углы -> любая свободная.
    """
    opponent_symbol = 'X' if bot_symbol == 'O' else 'O'
    board_size = len(board)

    # 1. Проверить, может ли бот выиграть
    win_move = find_winning_move(board, bot_symbol)
    if win_move != (-1, -1):
        return win_move

    # 2. Проверить, нужно ли блокировать оппонента
    block_move = find_winning_move(board, opponent_symbol)
    if block_move != (-1, -1):
        return block_move

    # 3. Занять центральную ячейку, если она свободна (для нечетных досок)
    if board_size % 2 != 0:
        center = board_size // 2
        if board[center][center] == '.':
            return (center, center)

    # 4. Занять свободный угол
    corners = [(0, 0), (0, board_size - 1), (board_size - 1, 0), (board_size - 1, board_size - 1)]
    random.shuffle(corners) # Перемешиваем, чтобы не всегда выбирать один и тот же угол
    for r, c in corners:
        if board[r][c] == '.':
            return (r, c)

    # 5. В противном случае, выбрать случайную свободную ячейку
    empty_cells = []
    for r in range(board_size):
        for c in range(board_size):
            if board[r][c] == '.':
                empty_cells.append((r, c))

    if empty_cells:
        return random.choice(empty_cells)
    
    # Этого не должно произойти, если игра корректно проверяет ничью
    return (-1, -1)