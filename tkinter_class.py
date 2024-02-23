import tkinter as tk
import requests
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Выводит json файл и сохраняет')
        self.geometry('600x600')

        self.label = tk.Label(self, text='введите какой ID вам нужен  : ')
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="сохранить и отабразить", command=self.get_text)

        self.label.pack()
        self.entry.pack()
        self.button.pack()

    def get_text(self):
        integer = int(self.entry.get())
        print(type(integer))
        url = f'https://jsonplaceholder.typicode.com/todos/{integer}'

        req = requests.get(url)
        os.mkdir('dz')
        with open(f'./dz/git{integer}.json','w') as file:
            file.write(req.text)
        g=req.text
        print(g)

if __name__ == "__main__":
    app = Application()
    app.mainloop()