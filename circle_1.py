from random import randint

#Загадываем рандомное число
number_x = randint(1,100)


def circle_1(number_player):
    attempt = 5
    while attempt != 1:
        if number_player > number_x:
            print(f'Неверно! Загаданное число < {number_player}\n')
            attempt = attempt - 1
            print(f'У вас осталось {attempt} попыток')
            number_player = int(input('Введите число: '))
            continue
            if attempt == 0:
                new_player_govno = player_govno.pop()

        elif number_player < number_x:
            print(f'Неверно! Загаданное число > {number_player}\n')
            attempt = attempt - 1
            print(f'У вас осталось {attempt} попыток')
            number_player = int(input('Введите число: '))
            continue
            if attempt == 0:
                new_player_govno = player_govno.pop()

        else:
            print('Верно!')
            new_computer_govno = computer_govno.pop()

