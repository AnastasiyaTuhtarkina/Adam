tablo = list(range(1,10))


def show():
    for i in range(3):
        print(f" {tablo[0 + i * 3]} | {tablo[1 + i * 3]} | {tablo[2 + i * 3]} ")
        print('----------')

def start():
    print('Приветствуем Вас в игре крестики-нолики!')
    print('Хотите ли сыграть?')
    ans = input('Ответьте: Yes или No ')
    if ans.lower() == 'yes':
        print('Отлично! Желаем удачи!')
    else:
        print('Очень жаль. Приходите позже!')    


def game_hod(n):
    valid = False
    while not valid:
        print('Пожалуйста, выберите номер поля на которое хотите сходить ') 
        show()
        hod = int(input())
        if hod >= 1 and hod <= 9:
            if str(tablo[hod - 1]) not in 'XO':
                tablo[hod - 1] = n
                valid = True
            else:
                print('Поле занято')  
        else:
            print('Введите незанятые поля от 1 до 9')                   

def chek_win():
    wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for w in wins:
        if tablo[w[0]] == tablo[w[1]] == tablo[w[2]]:
            return tablo[w[0]]
    return False


def game():
    counter = 0
    valid = False
    while not valid:
        show()
        if counter % 2 == 0:
            game_hod('X')
        else:
            game_hod('O')    
        counter += 1

        win = chek_win()
        if win:
            print(win, 'Выиграл!!!')
            valid = True
            break
        if counter == 9:
            print('Ничья. Попробуйте еще раз!!!')
            break
        show()

start()
game()