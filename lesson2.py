import random

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number_realAsString = input("Введите число \n")
summ = 0
for i in number_realAsString:
    if i != ',' and i != '.':
        summ += int(i)
print(f'сумма цифр равна {summ}')

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input("Введите число\n"))
multiplicat = 1
strM = "1"
for i in range(2, n +1):
    multiplicat *= i
    strM += ',' + str(multiplicat)
print(strM)

#Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
list_sequence = [(lambda a:(1+1/a)**a) (a) for a in range(1, n)]

print(f'последовательность {list_sequence} сумма {sum(list_sequence)}')

#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях.
 #Позиции хранятся в файле file.txt в одной строке одно число

n = int(input('Введите число\n'))
list_number = [(lambda a: random.randint(-n, n)) (a) for a in range(n)]
file_read = open('file.txt', 'r')
multiplicat = 1
for el in file_read.readlines():
    multiplicat *= list_number[int(el)]

file_read.close()
print(f'список {list_number}  произведение позиций из файла {multiplicat}')

#Реализуйте алгоритм перемешивания списка.
random.shuffle(list_number)
print(f' перемешанный список из предыдущего приимера {list_number}')



