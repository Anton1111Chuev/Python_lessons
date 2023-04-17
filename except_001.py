

#Реализуйте 3 метода, чтобы в каждом из них получить разные исключения
#Сделал сразу в одном методе 3 типа исключений
def met_01(a, b):
    res = 0
    try:
        res = a/b
        f = open(f'temp{res}.txt', "r")
        for line in f:
            print(line)
        f.close()
    except ZeroDivisionError as e:
        print("Деление на 0: " + str(e))
    except TypeError as e:
        print("Не верный тип: " + str(e))
    except FileNotFoundError as e:
        print("Не найден файл: " + str(e))
    return res

met_01(3, 0)
met_01(3, "фыва")
met_01(1, 1)

#Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив, каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.

def arr_minus_in(arr1, arr2):
    res = []
    for i in range(0, len(arr1) ):
        res.append(arr1[i] - arr2[i])
    return res

def arr_minus(arr1, arr2):
    try:
        if len(arr1) != len(arr2):
            raise IndexError ("Получилось исключение")
    except IndexError as e:
        print("Индекс за пределами массива : " + str(e))
    else:
        return arr_minus_in(arr1, arr2)

arr_minus ([1, 3, 3, 6], [3, 5, 7])

#Реализуйте метод, принимающий в качестве аргументов два целочисленных массива, и возвращающий новый массив, каждый элемент которого равен частному элементов двух входящих массивов в той же ячейке.
# Если длины массивов не равны, необходимо как-то оповестить пользователя.

def arr_div_in(arr1, arr2):
    res = []
    for i in range(0, len(arr1) ):
        try:
            res.append(arr1[i] / arr2[i])
        except ZeroDivisionError as e:
            raise ZeroDivisionError(" произошло деление на 0 ")
    return res

def arr_div(arr1, arr2):
    res = []
    try:
        if len(arr1) != len(arr2):
            raise IndexError ("Индекс за пределами массива")
        res = arr_div_in(arr1, arr2)
    except Exception as e:
        print("Исключение: " + str(e))
    else:
        return res

arr_div([1, 3, 3, 6], [3, 5, 7, 0 ])
arr_div([1, 3, 3, 6], [3, 5, 7])
