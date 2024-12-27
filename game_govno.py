import random
from instructions import instruction

#Список букв для игрока и компьютера
player_govno = ['О','Н','В','О','Г']
computer_govno = ['О','Н','В','О','Г']

#Создаем пустой список для накопления букв для игрока и компьютера
new_player_govno = []
new_computer_govno = []

name_player = input('Приветствую тебя в игре ГОВНО!\n Введите ваше имя: ')
choice = input(f'\n{name_player}, вы хотели бы ознакомиться с инструкцией? (да/нет): ')

if choice == 'да':
    instruction()
elif choice == 'нет':
    print('Тогда начинаем!\n')
else:
    print('\nВы ввели неверно!')
    choice = input(f'{name_player}, вы хотели бы ознакомиться с инструкцией? (да/нет): ')
