'''
Крестики нолики
Функция 1- отрисовка поля
Функция2- логика игры
Функция3- победа
Функция4- главная функция отвечает за запуск игры
'''
from itertools import count

list1=[1,2,3,4,5,6,7,8,9]#Клетки на крестиках ноликах

def print_boars():
    print("-"*13)
    for i in range(0,3):
        print(f"| {list1[0+i*3]} | {list1[1+i*3]} | {list1[2+i*3]} |")
        print("-"*13)
def logic_game(user_token):#ф-ция2 user_token- крестик или нолик
    valid = False
    while not valid: #while !False: пока Правда цикл работает:
        answer=int(input(f"Куда поставим {user_token}?"))
        if 1<=answer<=9:
            if str(list1[answer-1]) not in "X0":
                list1[answer-1]=user_token
                valid = True
            else:
                print("Эта клетка занята")
        else:
             print("Введене неверное число игрового поля. Введите число от 1 до 9")
def win():
    win_сoord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6), (1,4,7), (2,5,8),(0,4,8),(2,4,6))
    for i in win_сoord:
        if list1[i[0]]==list1[i[1]]==list1[i[2]]:
            return list1[i[0]]
    return False #не выигрыш
# win()
def main():
    counter=0 #Кол-во шагов, максимум 9
    win_player=False #Пока нет победителя
    while not win_player:
        print_boars()
        if counter%2==0:
            logic_game("X")
        else:
            logic_game("0")
        counter+=1
        if counter>4:#Проверяем на победу
            result=win()
            if result!= False:
                print_boars()
                print(f"Победил игрок {result}")
                win_player=True
                break
        if counter==9:
            print_boars()
            print("Ничья")
            break
main()
