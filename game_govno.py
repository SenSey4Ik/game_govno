import random
from instructions import instructions
from question_instructions import question_instructions
from circle_1 import circle_1




#Приветствие с игроком
name_player = input('Приветствую тебя в игре ГОВНО!\n Введите ваше имя: ')

#Ознакомление с инструкцией
choice = input(f'\n{name_player}, вы хотели бы ознакомиться с инструкцией? (да/нет): ')
question_instructions(choice)

number_player = int(input('Введите число: '))
circle_1(number_player)