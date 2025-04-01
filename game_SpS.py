import random

def get_user_turn():
    print("1-камень. 2-ножницы. 3-бумага. \n")
    while True:
        try:
            user_turn=int(input())
            if user_turn in range(1,4):
                break
        except:
            print("Только число от 1 до 3 !!!!!!")   
    return user_turn

def get_comp_turn():
    return random.randint(1,3)

def chek_round(human_turn, comp_turn):
    if human_turn == comp_turn:
        return "Ничья"
    elif human_turn == 1 and comp_turn == 2:
        return "Ты победил!"
    elif human_turn == 1 and comp_turn == 3:
        return "Ты проиграл!"
    elif human_turn == 2 and comp_turn == 3:
        return "Ты победил!"
    elif human_turn == 2 and comp_turn == 1:
        return "Ты проиграл!"
    elif human_turn == 3 and comp_turn == 2:
        return "Ты победил!"  
    elif human_turn == 3 and comp_turn == 1:
        return "Ты проиграл!" 
         
    # Основной цикл

total_game = 0
win_game = 0

while True:
    human_turn = get_user_turn()
    comp_turn = get_comp_turn()
    result = chek_round(human_turn, comp_turn)
    total_game += 1
    if result == "Ты победил!":
        win_game += 1
    print(result)
    print("Всего игр:", total_game, ". Побед:", win_game)
    user_choise = input("Сыграем ещё? 1-да, 0-нет")
    if user_choise == "0":
        break 