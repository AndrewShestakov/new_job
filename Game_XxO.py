import time

def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print("")
    print("")
def show_field(f): # Функция создания  поля игры
    a = 1 #Данная переменная-счетчик, необходима для создания нумерации строки и столбца
    f = [["- "] * 3 for j in range(3)]
    string = ''
    while a <= 3:
        string += (" " + str(a))
        a += 1
    print(*string)
    print("-" * (3 * 4 + 3)) # Разделяет визуально строки.
    for row, i in zip(field,string.split()):
        print(f"{i} {' ' .join(str(j) for j in row)}")
        print("-" * (3 * 4 + 3)) #

#show_field()
def ask(field, user):
    while True:
        cords  = input(f"\nХодит игрок {user}\nВведите две координаты :").split()
        if len(cords) != 2:
            print("\nВведите два числа через пробел")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print("\nВведены символы, не отвечающие условию,\nDведите целые положительные  числа")
            continue
        x, y = int(x), int(y)
        if x == 0 or y == 0 or x > 3 or y > 3:
            print("\nВы вышли за пределы поля,\nвведите корректные данные")
            continue
        x, y = x - 1, y - 1 #(-1) необходимо для корректного отбражения данных в игре
        if field[x][y] != "- |":
            print("\nДанная клетка занята")
            continue
        return x, y

def win_cords(f, user):
    def check_line(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
    for n in range(3):
         if check_line(f[n][0], f[n][1], f[n][2], user) or \
               check_line(f[0][n], f[1][n], f[2][n], user) or \
           check_line(f[0][0], f[1][1], f[2][2], user) or \
           check_line(f[0][2],f [1][1], f[2][0], user):
            return True
    return False
def replay():
    while True:
        replay = input("\nЖелаете еще поиграть?\ny -Да, n - Нет:")
        replay = replay.lower()
        if replay != "y" and replay != "n":
            print("\nВведите корректные данные\ny -Да, n - Нет:")
            continue
        if replay == "y":
            print("\nОтлично, играем")
            time.sleep(1)
            return

        else:
            print("\nСпасибо за игру!!!\n   ПОКА ПОКА!!!")
            time.sleep(3)
            break


def start_func(field):
    greet()
    count = 0
    while True:
        show_field(field)
        if count % 2 == 0:
            user = "Х |"
        else:
            user = "О |"
        x, y = ask(field, user)
        field[x][y] = user
        count += 1
        if count == 9:
            return print(show_field(field), "\nНичья")

        if win_cords(field, user):
            return print(f"\n{show_field(field)} \nПоздравляем! Победил игрок {user}!!!")


field = [["- |"] * 3 for j in range(3)]

start_func(field)
replay()


