from tkinter import *
import random
from tkinter import messagebox
from tkinter import ttk


def click_button():
    global inp, b1, win, resh, mis, k
    otv = inp.get()
    print(otv)
    if otv == '':
        messagebox.showerror("Ошибка", "Необходимо ввести число")
        win.destroy()
        run(k, resh)
    otv1 = int(otv)
    if otv1 == b1:
        k=2
        resh += 1
        msg1 = f"Молодец правильно!!! Твой счет: {resh} Продолжим дальше"
        messagebox.showinfo("Правильно!", msg1)
        win.destroy()
        run(k, resh)
    else:
        mis +=1
        if mis < 3:
            msg2 =f'Ну как так можно, давай еще думать!!! Количество неправильных ответов: {mis}'
            messagebox.showerror("Ошибка", msg2)
        
        
        if mis >= 3:
            messagebox.showerror("Ошибка", "Очень плохо, отдохни")
            win.destroy()            
        
        
def gen():
    global inp, b1, button_start, resh, score, comboExample, comboExample1
    if isinstance(comboExample, ttk.Combobox):
        msg_select.pack_forget()
        comboExample1 = comboExample.get()
        comboExample.destroy()
        comboExample = 0
    score.destroy()
    button_start.destroy()
    b1 = random.randint(10, 999)
    if comboExample1 == "3":
        a1 = random.randint(100, 999)
    elif comboExample1 == "2":
        a1 = random.randint(10, 99)
    else:
        messagebox.showerror("Ошибка", "Выбери на скольки значное число делить 2-х или 3-х?")
        win.destroy()
        run(k, resh)
    s1 = a1*b1
    msg = Label(text=f"Сколько будет {s1} : {a1} = ?")
    msg.pack()
    msg = Label(text="")
    msg.pack()
    inp = Entry()
    inp.pack()
    msg = Label(text="")
    msg.pack()
    button = Button(text="Ответить", command=click_button)
    button.pack()
      

def run(k, resh):
    global button_start, win, score, comboExample, msg_select
    win = Tk()
    win.geometry("400x250")
    win.title("Задания по математике")
    if k==1:
        score = Label(text=f'Ты решил {resh} примеров')
        score.pack()
        msg_select = Label(text="Выбери на скольки значное число делить 2-х или 3-х?")
        msg_select.pack()
        comboExample = ttk.Combobox(win, values=["2", "3"])
        comboExample.pack()
        msg = Label(text="")
        msg.pack()
        button_start = Button(text="Начнем игру", command=gen)
        button_start.pack()
    else:
        score = Label(text=f'Ты решил {resh} пример(ов)')
        score.pack()
        msg = Label(text="")
        msg.pack()
        button_start = Button(text="Новый пример", command=gen)
        button_start.pack()
    win.mainloop()

k=1
resh = 0
mis = 0
run(k, resh)
