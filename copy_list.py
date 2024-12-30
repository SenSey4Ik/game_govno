#Список букв для игрока и компьютера
player_govno = ['О','Н','В','О','Г']
computer_govno = ['О','Н','В','О','Г']

#Копируем список букв для игрока и компьютера
copy_player_govno = []
copy_computer_govno = []
def copy_list_player_govno():
    copy_player_govno = player_govno[:]
    return copy_player_govno

def copy_list_computer_govno():
    copy_computer_govno = computer_govno[:]
    return copy_computer_govno
