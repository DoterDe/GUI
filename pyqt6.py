from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QFileDialog, QVBoxLayout, QLineEdit
import sys
import requests
import os
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')

        self.widget = QWidget()
        self.label = QLabel()
        self.button = QPushButton('click me')
        self.layout = QVBoxLayout()
        self.entry = QLineEdit()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.entry)
        self.layout.addWidget(self.button)

        self.widget.setLayout(self.layout)
        self.button.clicked.connect(self.click)
        self.setCentralWidget(self.widget)

    def click(self):
        id = self.entry.text()
        response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
        data = response.json()

        if not os.path.exists('jsonplaceholder'):
            os.mkdir('jsonplaceholder')

        with open(f'./jsonplaceholder/data{id}.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.label.setText(f'Данные сохранены в файле data{id}.json')

app = QApplication([])
window = MainWindow()
window.show()
app.exec()