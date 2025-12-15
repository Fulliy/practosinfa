import random
from game_logic import TicTacToeGame
from stats_manager import ensure_stat_directory_exists

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