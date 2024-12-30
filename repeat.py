from circle_1 import circle_1
from copy_list import copy_list_player_govno, copy_list_computer_govno
repeat = ''

def repeat_game(repeat):
    if repeat == 'да':
        number_player = int(input('\nВведите число: '))
        circle_1(number_player)
    if repeat == 'нет':
        print('\nДо скорых встреч!')
    else:
        print('Вы не ответили на поставленный вопрос!')
        repeat = input('\nЖелаете сыграть снова? (да/нет)')
        repeat_game(repeat)