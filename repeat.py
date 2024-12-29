from circle_1 import circle_1
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