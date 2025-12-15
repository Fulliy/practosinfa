import os
import random
import datetime

class TicTacToeGame:
    def __init__(self, board_size, starting_player, game_mode):
        """
        Инициализация игры.
        
        :param board_size: размер игрового поля (N x N)
        :param starting_player: символ игрока, который ходит первым ('X' или 'O')
        :param game_mode: режим игры (1 - Человек vs Человек, 2 - Человек vs Бот)
        """
        self.board_size = board_size
        self.board = [['.' for _ in range(board_size)] for _ in range(board_size)]
        self.current_player = starting_player
        self.game_mode = game_mode
        self.moves_count = 0

    def print_board(self):
        """Выводит игровое поле в консоль."""
        print("\n  " + " ".join(str(i) for i in range(self.board_size)))
        for i, row in enumerate(self.board):
            print(f"{i} " + " ".join(row))
        print()

    def get_human_move(self):
        """
        Получает ход от человеческого игрока.
        
        :return: кортеж (row, col) с координатами хода
        """
        while True:
            try:
                move_str = input(f"Игрок {self.current_player}, введите ваш ход (строка столбец): ")
                parts = move_str.split()
                if len(parts) != 2:
                    print("Неверный формат. Введите два числа через пробел (строка и столбец).")
                    continue
                
                row, col = int(parts[0]), int(parts[1])
                
                if 0 <= row < self.board_size and 0 <= col < self.board_size:
                    if self.board[row][col] == '.':
                        return (row, col)
                    else:
                        print("Эта ячейка уже занята. Выберите другую.")
                else:
                    print(f"Координаты должны быть в диапазоне от 0 до {self.board_size - 1}.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите числа.")

    def find_winning_move(self, symbol):
        """
        Ищет ход, который позволит symbol выиграть или заблокировать победу оппонента.
        Возвращает (row, col) если найден выигрышный ход, иначе (-1, -1).
        """
        board_size = self.board_size

        # Проверка строк
        for r in range(board_size):
            count = 0
            empty_col = -1
            for c in range(board_size):
                if self.board[r][c] == symbol:
                    count += 1
                elif self.board[r][c] == '.':
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
                if self.board[r][c] == symbol:
                    count += 1
                elif self.board[r][c] == '.':
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
            if self.board[i][i] == symbol:
                count += 1
            elif self.board[i][i] == '.':
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
            if self.board[i][board_size - 1 - i] == symbol:
                count += 1
            elif self.board[i][board_size - 1 - i] == '.':
                empty_r, empty_c = i, board_size - 1 - i
            else:
                count = -1
                break
        if count == board_size - 1 and empty_r != -1:
            return (empty_r, empty_c)

        return (-1, -1) # Нет выигрышного хода

    def get_bot_move(self):
        """
        Вычисляет оптимальный ход для бота.
        Реализует стратегию: выигрыш -> блокировка -> центр -> углы -> любая свободная.
        """
        bot_symbol = self.current_player
        opponent_symbol = 'X' if bot_symbol == 'O' else 'O'
        board_size = self.board_size

        # 1. Проверить, может ли бот выиграть
        win_move = self.find_winning_move(bot_symbol)
        if win_move != (-1, -1):
            return win_move

        # 2. Проверить, нужно ли блокировать оппонента
        block_move = self.find_winning_move(opponent_symbol)
        if block_move != (-1, -1):
            return block_move

        # 3. Занять центральную ячейку, если она свободна (для нечетных досок)
        if board_size % 2 != 0:
            center = board_size // 2
            if self.board[center][center] == '.':
                return (center, center)

        # 4. Занять свободный угол
        corners = [(0, 0), (0, board_size - 1), (board_size - 1, 0), (board_size - 1, board_size - 1)]
        random.shuffle(corners) # Перемешиваем, чтобы не всегда выбирать один и тот же угол
        for r, c in corners:
            if self.board[r][c] == '.':
                return (r, c)

        # 5. В противном случае, выбрать случайную свободную ячейку
        empty_cells = []
        for r in range(board_size):
            for c in range(board_size):
                if self.board[r][c] == '.':
                    empty_cells.append((r, c))

        if empty_cells:
            return random.choice(empty_cells)
        
        # Этого не должно произойти, если игра корректно проверяет ничью
        return (-1, -1)

    def check_winner(self):
        """
        Проверяет, есть ли победитель на доске.
        
        :return: символ победителя ('X' или 'O'), 'DRAW' при ничье, или None если игра продолжается
        """
        board_size = self.board_size
        
        # Проверка строк
        for row in self.board:
            if all(cell == row[0] and cell != '.' for cell in row):
                return row[0]
        
        # Проверка столбцов
        for col in range(board_size):
            if all(self.board[row][col] == self.board[0][col] and self.board[row][col] != '.' for row in range(board_size)):
                return self.board[0][col]
        
        # Проверка главной диагонали
        if all(self.board[i][i] == self.board[0][0] and self.board[i][i] != '.' for i in range(board_size)):
            return self.board[0][0]
        
        # Проверка побочной диагонали
        if all(self.board[i][board_size - 1 - i] == self.board[0][board_size - 1] and self.board[i][board_size - 1 - i] != '.' for i in range(board_size)):
            return self.board[0][board_size - 1]
        
        # Проверка на ничью
        if self.moves_count == board_size * board_size:
            return "DRAW"
        
        return None

    def make_move(self, row, col):
        """
        Выполняет ход на указанную позицию.
        
        :param row: строка
        :param col: столбец
        :return: True если ход выполнен успешно, False в противном случае
        """
        if 0 <= row < self.board_size and 0 <= col < self.board_size and self.board[row][col] == '.':
            self.board[row][col] = self.current_player
            self.moves_count += 1
            return True
        return False

    def switch_player(self):
        """Переключает текущего игрока."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        """Запускает и управляет игровым процессом."""
        print(f"\nНачало игры! Размер поля: {self.board_size}x{self.board_size}")
        print("Игроки: X и O")
        
        while True:
            self.print_board()
            
            # Получение хода в зависимости от режима игры и текущего игрока
            if self.game_mode == 2 and self.current_player == 'O':  # Ход бота
                print("Ход бота...")
                row, col = self.get_bot_move()
            else:  # Ход человека
                row, col = self.get_human_move()
            
            # Выполнение хода
            if self.make_move(row, col):
                # Проверка результата игры
                result = self.check_winner()
                if result:
                    self.print_board()
                    if result == "DRAW":
                        print("Ничья!")
                        log_game_result("DRAW")
                    else:
                        print(f"Победил игрок {result}!")
                        log_game_result(f"{result}_WINS")
                    break
                
                # Переключение игрока
                self.switch_player()
            else:
                print("Неверный ход. Попробуйте снова.")

    @staticmethod
    def get_board_size_input():
        """
        Получает от пользователя размер игрового поля.
        
        :return: целое число - размер поля
        """
        while True:
            try:
                size_str = input("Введите размер игрового поля (N для поля NxN, минимум 3): ")
                size = int(size_str)
                if size >= 3:
                    return size
                else:
                    print("Размер поля должен быть не менее 3.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")


# Путь к директории и файлу статистики
STATS_DIR = "TicTacToeStats"
STATS_FILE = os.path.join(STATS_DIR, "game_results.txt")

def ensure_stat_directory_exists():
    """Убеждается, что директория для сохранения статистики существует."""
    try:
        if not os.path.exists(STATS_DIR):
            os.makedirs(STATS_DIR)
            print(f"Создана директория для статистики: {STATS_DIR}")
    except OSError as e:
        print(f"Ошибка при создании директории для статистики {STATS_DIR}: {e}")

def log_game_result(result):
    """
    Логирует результат игры в файл.
    :param result: Строка, описывающая результат игры (например, "X_WINS", "O_WINS", "DRAW").
    """
    ensure_stat_directory_exists() # Проверяем каждый раз на случай удаления
    try:
        with open(STATS_FILE, 'a') as f:
            log_entry = f"{datetime.datetime.now()}: {result}\n"
            f.write(log_entry)
        print(f"Результат игры залогирован в файл: {STATS_FILE}")
    except IOError as e:
        print(f"Ошибка при логировании результата игры в файл {STATS_FILE}: {e}")

def get_game_mode_input():
    """
    Получает от пользователя выбор режима игры (Человек vs Человек или Человек vs Бот).
    """
    while True:
        try:
            mode_str = input("Выберите режим игры (1 - Человек против Человека, 2 - Человек против Бота): ")
            mode = int(mode_str)
            if mode in [1, 2]:
                return mode
            else:
                print("Неверный ввод. Пожалуйста, введите 1 или 2.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число 1 или 2.")

def main():
    """Основная функция программы."""
    ensure_stat_directory_exists() # Создаем директорию для статистики

    print("Добро пожаловать в игру Крестики-нолики!")

    play_again = True
    while play_again:
        game_mode = get_game_mode_input() # Оценка 5: выбор режима
        board_size = TicTacToeGame.get_board_size_input() # Оценка 3: размер поля

        # Оценка 4: случайный выбор первого игрока
        starting_player = random.choice(['X', 'O'])
        print(f"Начинает игрок '{starting_player}'")

        game = TicTacToeGame(board_size, starting_player, game_mode)
        game.play_game()

        # Оценка 4: возможность запустить новую игру
        response = input("\nИгра завершена. Хотите сыграть еще? (да/нет): ").lower()
        play_again = (response == "да" or response == "yes")

    print("Спасибо за игру! До свидания.")

if __name__ == "__main__":
    main()