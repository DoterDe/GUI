
import tkinter as tk
import requests
from random import randint
import os
from tkinter import Tk, Label, Button 


window = tk.Tk()

window.title('Выводит json файл и сохраняет')
window.geometry('600x600')


def get_text():
    
    integer =int(entry.get()) 
    print(type(integer))
    url = f'https://jsonplaceholder.typicode.com/todos/{integer}'

    req = requests.get(url)
    os.mkdir('dz')
    with open(f'./dz/git{integer}.json','w') as file:
            file.write(req.text)
    g=req.text
    print(g)



label = Label(window, text='введите какой ID вам нужен  : ')
entry = tk.Entry(window)

button = tk.Button(window, text="сохранить и отабразить", command=get_text)
label.pack()
entry.pack()
button.pack()
window.mainloop()