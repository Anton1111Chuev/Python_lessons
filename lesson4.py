import math
import re
from re import search
from random import random, randint

#Вычислить число Пи c заданной точностью d
acc = 0.0001
k = 1
pi, pi_old = 0, 1
for i in range(1000000000):
    if abs(pi - pi_old) < acc:
        break
    pi_old = pi
    if i % 2 == 0 :
        pi += 4 / k
    else:
        pi -= 4 / k
    k += 2
print(pi)

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N
prime_factors = []
num_i = 200
num = num_i
while num % 2 == 0:
    prime_factors.append(2)
    num = num / 2

for i in range(3, int(math.sqrt(num)) + 1, 2):
    while num % i == 0:
        prime_factors.append(i)
        num = num / i
if num > 2:
    prime_factors.append(num)

print(f'Простые множители числа {num_i} = {prime_factors}')

#Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
line_num = '1112223445666'

lst = list(filter(lambda el: line_num.count(el) == 1, line_num))
print(f'Для последовательности {line_num} список неповторяющихся значений {lst}')

#Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
#многочлена и записать в файл многочлен степени k
k = 5
file = open('file1.txt', 'w')


list_k = list(randint(-100, 100) for a in range(k))
def actioniter(num, iter_):
    if num == 0:
        return ''
    zn = '+' if list_k[i] > 0 else ''
    if iter_ == 1:
        return f'{zn}{num}x'
    elif iter_ == 0:
        return f'{zn}{num}'
    return f'{zn}{num}x^{iter_}'

for i in range(k):
    list_k[i] = actioniter( list_k[i], i)
file.write(''.join(list_k))
file.close()

#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.
indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }


def degree(a: int):
    degrees = ""
    temp = str(a)
    for char in temp:
        degrees += indexes[char] or ""
    return degrees


st1 = "17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0"
st2 = "23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0"
max_step = 20
dict1 = {a: 0 for a in range(max_step)}
dict2 = {a: 0 for a in range(max_step)}
dict_sum = {a: 0 for a in range(max_step)}

st1 = st1.replace(" ", "")
st2 = st2.replace(" ", "")
def str_tonum(st, reg):
    reg1 = '[-+]?\d+'
    res = re.search(reg, st)
    if res:
        return int(re.search(reg1, res.group(0)).group(0))
    return 0

dict1[0] = str_tonum(st1, '[-+]\d+\W')
dict2[0] = str_tonum(st2, '[-+]\d+\W')
dict_sum[0] = dict1[0] + dict2[0]
dict1[1] = str_tonum(st1, '[-+]?\d+x[+-=]')
dict2[1] = str_tonum(st2, '[-+]?\d+x[+-=]')
dict_sum[1] = dict1[1] + dict2[1]

for i in range(2, max_step):
    step = degree(str(i))
    dict1[i] = str_tonum(st1, f'[-+]?\d+x{degree(str(i))}[+-=]')
    if dict1[i] == 0 and st1.find('x' + step) > -1:
        dict1[i] = 1
    dict2[i] = str_tonum(st2, f'[-+]?\d+x{degree(str(i))}[+-=]')
    if dict2[i] == 0 and st2.find('x' + step) > -1:
        dict2[i] = 1
    dict_sum[i] = dict1[i] + dict2[i]

result = ""
for i in range(max_step - 1, 1, -1):
    el = dict_sum[i]
    zn = '+' if el > 0 else ""
    if el != 0:
        result += zn + str(el) + "x" + degree(i)

if dict_sum[1] != 0:
    zn = '+' if dict_sum[1] > 0 else ""
    result += zn + str(dict_sum[1]) + 'x'
if dict_sum[0] != 0:
    zn = '+' if dict_sum[0]> 0 else ""
    result += zn + str(dict_sum[0])
result += " = 0 "
print(f' {st1}  \n {st2} \n результат \n {result}')
f = open('file2.txt', 'w')
f.write(str(result.encode()))
f.close()