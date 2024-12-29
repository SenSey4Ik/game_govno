from random import randint

number_player = int
#Загадываем рандомное число
number_x = randint(1,100)


#Список букв для игрока и компьютера
player_govno = ['О','Н','В','О','Г']
computer_govno = ['О','Н','В','О','Г']

#Создаем пустой список для накопления букв для игрока и компьютера
new_player_govno = []
new_computer_govno = []

def circle_1(number_player, new_player_govno='',new_computer_govno=''):
    while new_player_govno or new_computer_govno != ['Г','О','В','Н','О']:
        attempt = 5
        while attempt != 1:
            if number_player > number_x:
                print(f'Неверно! Загаданное число < {number_player}\n')
                attempt = attempt - 1
                print(f'У вас осталось {attempt} попыток')
                number_player = int(input('Введите число: '))
                if attempt == 1:
                    new_player_govno = player_govno.pop()

                    print('\nВы получаете букву!')
                    print(new_player_govno)
                    continue

            elif number_player < number_x:
                print(f'Неверно! Загаданное число > {number_player}\n')
                attempt = attempt - 1
                print(f'У вас осталось {attempt} попыток')
                number_player = int(input('Введите число: '))
                if attempt == 1:
                    new_player_govno = player_govno.pop()

                    print('\nВы получаете букву!')
                    print(new_player_govno)
                    continue


            else:
                new_computer_govno = computer_govno.pop()
                print('\nВерно!')
                print('Компьютер получает букву!')
                print(new_computer_govno)

