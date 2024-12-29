from random import randint

number_player = int
#Загадываем рандомное число
number_x = randint(1,100)


#Список букв для игрока и компьютера
player_govno = ['О','Н','В','О','Г']
computer_govno = ['О','Н','В','О','Г']

#Копируем список букв для игрока и компьютера
copy_player_govno = []
copy_computer_govno = []

#Промежуточный список
letter_govno = []

#Создаем пустой список для накопления букв для игрока и компьютера
new_player_govno = []
new_computer_govno = []


def circle_1(number_player, new_player_govno=[],new_computer_govno=[],the_end=''):
    while True:
        if the_end == 'Вы проиграли! Вы ГОВНО':
            break
        attempt = 5
        while True and attempt != 1:
            if number_player > number_x:
                print(f'Неверно! Загаданное число < {number_player}\n')
                attempt = attempt - 1
                print(f'У вас осталось {attempt} попыток')
                number_player = int(input('Введите число: '))
                if attempt == 1:
                    copy_player_govno = player_govno[:]
                    letter_govno = copy_player_govno.pop()
                    new_player_govno.append(letter_govno)
                    if new_player_govno != ['Г','О','В','Н','О']:
                        print('\nВы получаете букву!')
                        print(new_player_govno)
                        number_player = int(input('\nВведите число: '))
                        continue
                    else:
                        the_end = print('Вы проиграли! Вы ГОВНО')
                        the_end = 'Вы проиграли! Вы ГОВНО'


            elif number_player < number_x:
                print(f'Неверно! Загаданное число > {number_player}\n')
                attempt = attempt - 1
                print(f'У вас осталось {attempt} попыток')
                number_player = int(input('Введите число: '))
                if attempt == 1:
                    copy_player_govno = player_govno[:]
                    letter_govno = copy_player_govno.pop()
                    new_player_govno.append(letter_govno)
                    if new_player_govno != ['Г', 'О', 'В', 'Н', 'О']:
                        print('\nВы получаете букву!')
                        print(new_player_govno)
                        number_player = int(input('\nВведите число: '))
                        continue
                    else:
                        the_end = print('Вы проиграли! Вы ГОВНО')
                        the_end = 'Вы проиграли! Вы ГОВНО'


            else:
                copy_computer_govno = computer_govno[:]
                letter_govno = copy_computer_govno.pop()
                new_computer_govno.append(letter_govno)
                if new_computer_govno != ['Г', 'О', 'В', 'Н', 'О']:
                    print('\nВерно!')
                    print('Компьютер получает букву!')
                    print(new_computer_govno)
                    number_player = int(input('\nВведите число: '))

                else:
                    the_end = print('Вы победили! Компьютер ГОВНО')
                    the_end ='Вы проиграли! Вы ГОВНО'



