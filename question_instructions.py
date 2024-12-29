from instructions import instructions

name_player = ''
choice = ''


#Цикл ответа на вопрос с инструкцией
def question_instructions(choice):
    while True:
        if choice == 'да':
            instructions()
            break
        elif choice == 'нет':
            print('Тогда начинаем!\n')
            break
        else:
            print('\nВы не ответили на поставленный вопрос!')
            choice = input(f'{name_player}, вы хотели бы ознакомиться с инструкцией? (да/нет): ')
            continue