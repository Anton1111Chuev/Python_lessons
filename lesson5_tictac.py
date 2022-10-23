import tkinter
from tkinter import *
import tkinter.messagebox as mb
from random import randint

window = Tk()
window.title("КрестикиНолики")
window.geometry('200x250')
window.size()
mult = 60
arr_btn = [[0,0,0], [0,0,0], [0,0,0]]
count_move = 0



class MyBtn(tkinter.Button):
    def __init__(self, form, col, row):
        self.is_input = False
        self.value = ""
        super(MyBtn, self).__init__(form, command=lambda x=col, y=row: clicked(x, y))
        self.place(x=col*mult, y=row*mult, width=mult, height=mult)

    def settext(self, text):
        self.configure(text=text)
        self.value = text
        self.is_input = True


def clicked(x, y):
    global arr_btn
    btn = arr_btn[x][y]
    if btn.is_input:
        return None
    btn.settext('X')
    analis(x, y)


def checkWin(text, x, y):
    global  arr_btn, count_move, window
    if count_move == 9:
        mb.showinfo("Результат",  "Ничья!")
        return True
    sumX, sumY, sumD, sumD_ = 0, 0, 0, 0
    for i in range(3):
        if arr_btn[x][i].value == text:
            sumX += 1
        if arr_btn[i][y].value == text:
            sumY += 1
        if arr_btn[i][i].value == text:
            sumD += 1
        if arr_btn[i][2-i].value == text:
            sumD_ += 1
    if sumX == 3 or sumY == 3 or sumD == 3 or sumD_ == 3:
        if text == 'X':
            mb.showinfo("Результат", "Вы выиграли!")
        else:
            mb.showinfo("Результат", "Вы проиграли!")
        return True


def analis(x, y):
    global count_move, window
    count_move += 1
    if checkWin("X", x, y):
        return
    x, y = getMove()
    if checkWin("O", x, y):
        return
    count_move += 1

    #checkWin("O", x, y )

def getMove():
    sumX_D, sumO_D = 0, 0
    sumX_D_, sumO_D_ = 0, 0
    for i in range(3):
        sumX_G, sumO_G = 0, 0
        sumX_V, sumO_V = 0, 0

        if arr_btn[i][i].value == "O":
            sumO_D += 1
        elif arr_btn[i][i].value == "X":
            sumX_D += 1
        if arr_btn[i][2-i].value == "O":
            sumO_D_ += 1
        elif arr_btn[i][2-i].value == "X":
            sumX_D_ += 1

        for j in range(3):
            if arr_btn[i][j].value == "O":
                sumO_G += 1
            elif arr_btn[i][j].value == "X":
                sumX_G += 1
            if arr_btn[j][i].value == "O":
                sumO_V += 1
            elif arr_btn[j][i].value == "X":
                sumX_V += 1

        if sumO_G == 2 and sumX_G == 0:
            for k in range(3):
                if arr_btn[i][k].value == "":
                    arr_btn[i][k].settext('O')
                    return (i, k)
        if sumO_V == 2 and sumX_V == 0:
            for k in range(3):
                if arr_btn[k][i].value == "":
                    arr_btn[k][i].settext('O')
                    return (k, i)
        if sumO_G == 0 and sumX_G == 2:
            for k in range(3):
                if arr_btn[i][k].value == "":
                    arr_btn[i][k].settext('O')
                    return (i, k)
        if sumO_V == 0 and sumX_V == 2:
            for k in range(3):
                if arr_btn[k][i].value == "":
                    arr_btn[k][i].settext('O')
                    return (k, i)
    if sumO_D == 2 and sumX_D == 0:
        for k in range(3):
            if arr_btn[k][k].value == "":
                arr_btn[k][k].settext('O')
                return (k, k)
    if sumO_D_ == 2 and sumX_D_ == 0:
        for k in range(3):
            if arr_btn[k][2-k].value == "":
                arr_btn[k][2-k].settext('O')
                return (k, 2-k)
    if sumO_D == 0 and sumX_D == 2:
        for k in range(3):
            if arr_btn[k][k].value == "":
                arr_btn[k][k].settext('O')
                return (k, k)
    if sumO_D_ == 0 and sumX_D_ == 2:
        for k in range(3):
            if arr_btn[k][2-k].value == "":
                arr_btn[k][2-k].settext('O')
                return (k, 2-k)
    while True:
        pointX = randint(0, 2)
        pointY = randint(0, 2)
        if not arr_btn[pointX][pointY].is_input:
            arr_btn[pointX][pointY].settext('O')
            return (pointX, pointY)



def init():
    global window, arr_btn
    btn = Button(window, text="Начать заново", command=init)
    btn.place(x=1, y=3*mult + 5, width=mult*3, height=mult)
    arr_btn = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(3):
        arr_btn.append([])
        for j in range(3):
            arr_btn[i][j] = MyBtn(window, i, j)

a = analis
init()
window.bind_class(analis)
window.mainloop()