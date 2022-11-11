import json
import tkinter as tk
from tkinter import Entry, Button, messagebox
from tkinter import Tk
from tkinter.ttk import Label
from model import PhoneDirectory
from adress_path import *
import tkinter.filedialog as fd



def clicked():
    inp_text = txt.get()
    if not inp_text:
        return
    text = get_action(phone_directory=phone_directory, action="get_by_name", name=inp_text)
    message_result(text, "Результаты поиска")


def clicked_save_json():
    text = get_action(phone_directory=phone_directory, action="save_json")
    message_result(text)

def clicked_save_csv():
    text = get_action(phone_directory=phone_directory, action="save_csv")
    message_result(text)

def clicked_load_json():
    filetypes = (("Текстовый файл", "*.txt"),)
    filename = fd.askopenfilename(title="Открыть файл", filetypes=filetypes)
    if filename:
        text = get_action(phone_directory=phone_directory, action="load_json", filename=filename)
        message_result(text)

def clicked_load_scv():
    filetypes = (("Файл", "*.csv"),)
    filename = fd.askopenfilename(title="Открыть файл", filetypes=filetypes)
    if filename:
        text = get_action(phone_directory=phone_directory, action="load_csv", filename=filename)
        message_result(text)


def message_result(text, descr = "Результат: "):
    if not text:
        return
    messagebox.showinfo(descr, text)





phone_directory = PhoneDirectory() # Кэш соединения с БД, можно и не делать
window = Tk()
window.geometry('400x250')
window.title("Телефонный справочник")

lbl = tk.Label(window, text="Введите для поиска номера")
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)

btn_searsh = Button(window, text="Искать имя в справочнике", command=clicked)
btn_searsh .grid(column=2, row=0)

btn_savejson = Button(window, text="Сохранить json", command=clicked_save_json)
btn_savejson.grid(column=0, row=6)

btn_save_csv = Button(window, text="Сохранить csv", command=clicked_save_csv)
btn_save_csv.grid(column=1, row=6)

btn_load_json = Button(window, text="Загрузить json", command=clicked_load_json)
btn_load_json.grid(column=0, row=7)

btn_load_csv = Button(window, text="Загрузить csv", command=clicked_load_scv)
btn_load_csv.grid(column=1, row=7)

window.mainloop()


