# Проба кода для консольного варианта крестиков-ноликов
playing_field = ["-", "1", "2", "3",
                 "1", "-", "-", "-",
                 "2", "-", "-", "-",
                 "3", "-", "-", "-"]

win_comb = [(5, 6, 7), (9, 10, 11), (13, 14, 15), (5, 9, 13), (6, 10, 14), (7, 11, 15), (5, 10, 15), (7, 10, 13)]


def print_field():
    for i in range(4):
        print("|", playing_field[i * 4], playing_field[i * 4 + 1], playing_field[i * 4 + 2], playing_field[i * 4 + 3],
              "|")


def move(pl_token):
    while True:
        pl_col = int(input(f"Введите столбец для {pl_token} "))
        pl_row = int(input(f"Введите ряд для {pl_token} "))
        pl_move = pl_col + pl_row * 4
        if pl_move in range(1, 4) and 8 and 12:
            print("Ошибка ввода. Повторите.")
            continue
        if pl_move > 15:
            print("Ошибка ввода. Повторите.")
            continue
        if str(playing_field[pl_move]) in "XO":
            print("Клетка занята. Повторите ход.")
            continue
        playing_field[pl_move] = pl_token
        break


def check_win():
    for comb in win_comb:
        if (playing_field[comb[0]] == playing_field[comb[1]] == playing_field[comb[2]] in "XO"):
            return playing_field[comb[1]]
    else:
        return False


def tic_tac_toe():
    status = 0
    while True:
        print_field()
        if status % 2 == 0:
            move("X")
        else:
            move("O")
        if status > 3:
            winner = check_win()
            if winner:
                print_field()
                print(winner, "выиграл!")
                break
        status += 1
        if status > 8:
            print_field()
            print("Ничья!")
            break


tic_tac_toe()
