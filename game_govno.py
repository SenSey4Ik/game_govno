import random
from instructions import instruction
import circle_1

#Список букв для игрока и компьютера
player_govno = ['О','Н','В','О','Г']
computer_govno = ['О','Н','В','О','Г']

#Создаем пустой список для накопления букв для игрока и компьютера
new_player_govno = []
new_computer_govno = []


name_player = input('Приветствую тебя в игре ГОВНО!\n Введите ваше имя: ')
choice = input(f'\n{name_player}, вы хотели бы ознакомиться с инструкцией? (да/нет): ')

#Цикл ответа на вопрос с инструкцией
while True:
    if choice == 'да':
        instruction()
        break
    elif choice == 'нет':
        print('Тогда начинаем!\n')
        break
    else:
        print('\nВы не ответили на поставленный вопрос!')
        choice = input(f'{name_player}, вы хотели бы ознакомиться с инструкцией? (да/нет): ')
        continue

number_player = int(input('Введите число: '))

circle_1.circle_1(number_player)