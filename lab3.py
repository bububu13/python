from tkinter import *
import random
import string
from PIL import Image, ImageTk

def generate_key():
    key_input: str = txt.get()
    ps.configure(text='')
    try:
        num = str(int(key_input, 16))
        print(num)
    except ValueError:
        res.configure(text='Это не HEX число')
        return

    if len(num)<5:
        ps.configure(text=f'Число оказалось {len(num)} значным. В начале было добавлено {5 - len(num)} нулей')
        num = num.zfill(5)


    first_three = num[:3]
    second_two = num[-2:]

    alphabet = string.ascii_uppercase + string.digits

    blocks = []

    for i in range(3):
        block_chars = [random.choice(alphabet) for j in range(4) ]
        block_chars.append(first_three[i])
        random.shuffle(block_chars)
        blocks.append("".join(block_chars))

    key = f'{blocks[0]}-{blocks[1]}-{blocks[2]} {second_two}'
    res.configure(text=key)
    return



window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('500x500')


t = Image.open("Screenshot_20260603-124121.png")
bg_resized = t.resize((500, 500))
bg_photo = ImageTk.PhotoImage(bg_resized)
bg_label = Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)


lbl = Label(window, text="Генератор ключей", font=("Arial Bold", 20))
lbl.grid(column=0, row=0, columnspan=3)


entr = Label(window, text="Введите 5-значное HEX число")
entr.grid(column=0, row=1,padx=10, pady=10)

txt = Entry(window,width=10)
txt.grid(column=1, row=1, padx=10,pady=10)

btn = Button(window, text="Сгенерировать", command=generate_key)
btn.grid(column=2,row=1,padx=10,pady=10)

txt2 = Label(window, text="Ваш ключ:")
txt2.grid(column=0,row=2,pady=10)

res = Label(window, text='')
res.grid(column=1,row=2,pady=10)

ps = Label(window, text='', anchor='center')
ps.grid(column=0,row=3,columnspan=3)
window.mainloop()









