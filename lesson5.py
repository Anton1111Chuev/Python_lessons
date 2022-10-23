import re

#1.Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
text = "qweqweабв нормальное словоСабв нормальное слово"
lst = text.split(' ')
print(lst)
lst = list(filter(lambda x: not 'абв' in x,  lst))
print(" ".join(lst))

#2.Создайте программу для игры с конфетами человек против человека
#см файл lesson5_candy_game

#3.Создайте программу для игры в ""Крестики-нолики"".
#см файл lesson5_tictac

#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.
def code(text):
    lst1 = [text[0]]
    k = 1
    for i in range(1, len(text1)):
        if text[i] == text[i - 1]:
            k += 1
        else:
            if k > 1:
                lst1.append(str(k))
                k = 1
            lst1.append(text[i])
    return  ("".join(lst1))

def decode(text):
    result = ''
    k = ''
    for i in text:
        if i.isdigit():
            k += i
        else:
            if k != '':
                result += i * int(k)
            else:
                result += i
            k = ''
    return result


file = open('file4.txt', 'r')
text1 = file.read()
file.close()

cod = code(text1)
decod = decode(cod)

res = f'Исходный текст {text1} \nКодированный {cod} \nДекодированный {decod}'
print(res)

file = open('file5.txt', 'w')
text1 = file.write(res)
file.close()







