# Игровое поле (список из 9 элементов)
board = [' '] * 9


# Функция отображения игрового поля
def show_board():
    for i in range(3):
        print(f" {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} ")
        if i < 2:
            print("-----------")


# Проверка победы
def check_win():
    # Все возможные выигрышные комбинации
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # строки
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # столбцы
        [0, 4, 8], [2, 4, 6]  # диагонали
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != ' ':
            return board[a]  # возвращает 'X' или 'O'

    return 'Ничья' if ' ' not in board else None


# Основной игровой цикл
def game():
    player = 'X'  # Первый игрок

    while True:
        show_board()

        # Ход игрока
        while True:
            try:
                move = int(input(f"Игрок {player}, введите номер клетки (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == ' ':
                    break
                print("Некорректный ход! Попробуйте еще раз.")
            except ValueError:
                print("Введите число от 1 до 9!")

        board[move] = player

        # Проверка результата
        result = check_win()
        if result:
            show_board()
            print("Ничья!" if result == 'Ничья' else f"Игрок {result} победил!")
            break

        player = 'O' if player == 'X' else 'X'  # Смена игрока


# Запуск игры
print("Добро пожаловать в Крестики-Нолики!")
print("Клетки пронумерованы от 1 до 9, как на телефоне")
game()