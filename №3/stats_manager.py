import os
import datetime

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