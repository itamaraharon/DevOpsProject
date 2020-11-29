#!/usr/bin/env python3

import tkinter as tk
import docker
from os import system
import tkinter.font as font


TEXT_LINE = " "
COLOR_F = '#339cff'
CLIENT_D = docker.from_env()


def ERROR():
    text.delete(0.0, tk.END)
    text.insert(tk.END, "ERROR")


def ENTER_CON():
    text.delete(0.0, tk.END)
    text.insert(tk.END, 'Enter name container')


def IMAGES():
    co_list = (CLIENT_D.images.list())
    text_line = " "
    i = 0
    while i < len(co_list):
        var = (co_list[i])
        text_line = '{}{}{}'.format(text_line, var, "\n")
        i += 1
    return text_line


def CONTAINERS():
    co_list = (CLIENT_D.containers.list(list))
    text_line = ' '
    i = 0
    while i < len(co_list):
        var = str(co_list[i])
        text_line = '{}{}{}'.format(text_line, var, "\n")
        i += 1
    return text_line


def ALL_CONTAINERS():
    text.delete(0.0, tk.END)
    text.insert(tk.END, CONTAINERS())


def ALL_IMAGES():
    co_list = (CLIENT_D.images.list())
    if len(co_list) is 0:
        text.delete(0.0, tk.END)
        text.insert(tk.END, "No images")
    else:
        text.delete(0.0, tk.END)
        text.insert(tk.END, IMAGES())


def DOWNLOAD_IMAGE():
    image_1 = Entry1.get()
    ver = Entry3.get()
    Entry1.delete(0, tk.END)
    Entry3.delete(0, tk.END)
    Entry3.insert(tk.END, "latest")
    text.insert(tk.END, image_1)
    if image_1 != '' and ver != '':
        try:
            CLIENT_D.images.pull("{}:{}".format(image_1, ver))
            text.delete(0.0, tk.END)
            text.insert(tk.END, "Successfully! \npull {}:{}".format(image_1, ver))
        except():
            ERROR()
    else:
        text.delete(0.0, tk.END)
        text.insert(tk.END, 'Enter image or version')


def RUN_CON():
    con = Entry2.get()
    text.delete(0.0, tk.END)
    if con != '':
        try:
            system('gnome-terminal -x bash -c "docker run -it {} bash; exec bash"'.format(con))
            Entry1.delete(0, tk.END)
            text.insert(tk.END, "Successfully")
        except():
            ERROR()
    else:
        ENTER_CON()


def REMOVE_IMAGE():
    image_1 = Entry1.get()
    Entry1.delete(0, tk.END)
    ver = Entry3.get()
    Entry3.delete(0, tk.END)
    Entry3.insert(tk.END, "latest")
    text.insert(tk.END, image_1)
    if image_1 != '' and ver != '':
        if image_1 in IMAGES():
            try:
                CLIENT_D.images.remove("{}:{}".format(image_1, ver))
                text.delete(0.0, tk.END)
                text.insert(tk.END, "Successfully! \nDelete {}:{}".format(image_1, ver))
            except():
                ERROR()
        else:
            text.delete(0.0, tk.END)
            text.insert(tk.END, "not exist")
    else:
        text.delete(0.0, tk.END)
        text.insert(tk.END, 'Enter image or version')


def REMOVE_CON():
    rm = Entry2.get()
    Entry2.delete(0, tk.END)
    text.delete(0.0, tk.END)
    if rm != "":
        if rm in IMAGES():
            try:
                container_s = CLIENT_D.containers.get(rm)
                container_s.remove()
                text.insert(tk.END, "Successfully \nDelete {}!".format(rm))
            except():
                ERROR()
        else:
            text.delete(0.0, tk.END)
            text.insert(tk.END, "not exist")
    else:
        ENTER_CON()


def STOP_CON():
    rm = Entry2.get()
    Entry2.delete(0, tk.END)
    if rm != '':
        if rm in CONTAINERS():
            try:
                container_s = CLIENT_D.containers.get(rm)
                container_s.stop()
                text.insert(tk.END, "Successfully \n{} stop".format(rm))
            except():
                ERROR()
        else:
            text.delete(0.0, tk.END)
            text.insert(tk.END, "not exist")
    else:
        ENTER_CON()


root = tk.Tk()

canvas = tk.Canvas(root, height=620, width=650)
canvas.grid()

frame = tk.Frame(root, bg=COLOR_F)
frame.place(relheight=1, relwidth=1)

my = tk.Label(root)
my.place(x=20, y=160, relheight=0.7, relwidth=0.6)
text = tk.Text(my, bg='#66e1d2')
text.grid(row=0, column=1)
scrollbar = tk.Scrollbar(my)
text.config(yscrollcommand=scrollbar.set)
scrollbar.grid(row=0, column=0, sticky=tk.NSEW)

myFont = font.Font(family='Helvetica', size=20, weight='bold')

lbl1 = tk.Label(frame, text="DOCKER GUI", fg='blue', bg=COLOR_F)
lbl1['font'] = myFont
lbl1.place(relx=0.5, y=28, anchor='center')

lbl2 = tk.Label(frame, text='Enter Image:', bg=COLOR_F)
lbl2.place(x=10, y=60)

lbl3 = tk.Label(frame, text='Enter Container: ', bg=COLOR_F)
lbl3.place(x=10, y=110)

lbl4 = tk.Label(frame, text='Version: ', bg=COLOR_F)
lbl4.place(x=250, y=60)

Entry1 = tk.Entry(frame)
Entry1.place(x=130, y=60, relheight=0.04, relwidth=0.18)

Entry2 = tk.Entry(frame)
Entry2.place(x=130, y=110, relheight=0.04, relwidth=0.18)

Entry3 = tk.Entry(frame)
Entry3.place(x=310, y=60, relheight=0.04, relwidth=0.16)
Entry3.insert(tk.END, "latest")

btn1 = tk.Button(frame, text="Download", command=lambda: DOWNLOAD_IMAGE())
btn1.place(x=435, y=60, relheight=0.04, relwidth=0.15)

btn2 = tk.Button(frame, text="run", command=lambda: RUN_CON())
btn2.place(x=260, y=110, relheight=0.04, relwidth=0.15)

btn3 = tk.Button(frame, text="Delete", command=lambda: REMOVE_IMAGE())
btn3.place(x=540, y=60, relheight=0.04, relwidth=0.15)

btn4 = tk.Button(frame, text="Delete", command=lambda: REMOVE_CON())
btn4.place(x=510, y=110, relheight=0.04, relwidth=0.15)

btn4 = tk.Button(frame, text="Stop", command=lambda: STOP_CON())
btn4.place(x=385, y=110, relheight=0.04, relwidth=0.15)

btn6 = tk.Button(frame, text='show all images', command=lambda: ALL_IMAGES())
btn6.place(x=460, y=230, relheight=0.08, relwidth=0.25)

btn7 = tk.Button(frame, text='show all containers', command=lambda: ALL_CONTAINERS())
btn7.place(x=460, y=160, relheight=0.08, relwidth=0.25)

root.mainloop()
