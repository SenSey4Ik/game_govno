import random
from instructions import instructions
from question_instructions import question_instructions
from circle_1 import circle_1
from repeat import repeat_game
from copy_list import copy_list_player_govno, copy_list_computer_govno



#Приветствие с игроком
name_player = input('Приветствую тебя в игре ГОВНО!\n Введите ваше имя: ')

#Ознакомление с инструкцией
choice = input(f'\n{name_player}, вы хотели бы ознакомиться с инструкцией? (да/нет): ')
question_instructions(choice)

#Запрашиваем число у игрока, чтобы войти войти в цикл
number_player = int(input('Введите число: '))
circle_1(number_player)

#Обновляем список буквами
copy_list_player_govno()
copy_list_computer_govno()

#Предлагаем игроку сыграть заново
repeat = input('\nЖелаете сыграть снова? ')
repeat_game(repeat)