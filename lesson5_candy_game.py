from random import randint

count_candy = 115
max_candy = 28
is_moveBot = randint(0, 1) == 1
print(f'Начало игры \nВсего конфет {count_candy}, максимально можно взять {max_candy}, первый ход компьютера {is_moveBot}')
k_candy = 0
def inpCandy():
    try:
        n = int(input("введите количество конфет "))
        if n < 1 or n > max_candy:
            raise Exception("")
        return n
    except:
        print("вы ввели неккоректное число, попробуте еще раз")
        inpCandy()

while count_candy >=0:
    if is_moveBot:
        if count_candy <= max_candy:
            k_candy = count_candy
            print(f'Выиграл бот его ход {k_candy}')
            break
        else:
            k_candy = max_candy - count_candy%max_candy + 1
            print(f'бот взял {k_candy} конфет')
    else:
        if count_candy <= max_candy:
            print(f'Поздравляю вы выиграли')
            break
        else:
            k_candy = inpCandy()

    count_candy -= k_candy
    is_moveBot = not is_moveBot
    print(f'Осталось конфет {count_candy}')





