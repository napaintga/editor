
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, 
    QListWidget, QPushButton, QHBoxLayout, QVBoxLayout, QFileDialog)
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
app =QApplication([])
win = QWidget()
win.resize(600,300)
win.setWindowTitle("Easy Editor")


lb_image= QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()

btn_left = QPushButton("Ліво")
btn_right = QPushButton("Право")
btn_flip =QPushButton('Відзеркалити')
btn_sharp = QPushButton('Різкість')
btn_blur = QPushButton('бЛЮР')

btn_sharp.setStyleSheet('''
    QPushButton {
        background-color: red;
    }
    QPushButton:hover {
        background-color: purple;
    }
''')

btn_dir.setStyleSheet('''
    QPushButton {
        background-color: pink;
    }
    QPushButton:hover {
        background-color: darkpink;
    }
''')

btn_flip.setStyleSheet('''
    QPushButton {
        background-color: yellow;
    }
    QPushButton:hover {
        background-color: darkyellow;
    }
''')


btn_left.setStyleSheet('''
    QPushButton {
        background-color: green;
    }
    QPushButton:hover {
        background-color: darkgreen;
    }
''')

btn_right.setStyleSheet('''
    QPushButton {
        background-color: pink;
    }
    QPushButton:hover {
        background-color: darkpink;
    }
''')

row = QHBoxLayout()

row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_flip)
row.addWidget(btn_sharp)
row.addWidget(btn_blur)

col1=QVBoxLayout()
col2=QVBoxLayout()


col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)
col2.addLayout(row)

main_layout = QHBoxLayout()
main_layout.addLayout(col1)
main_layout.addLayout(col2)
win.setLayout(main_layout)

workdir = ""
def filter(files, extensions):
    result = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                result.append(file)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showlistimage():
    ext = ['png', 'jpg', 'jpeg', 'jfif', 'gif', 'svg']
    chooseWorkdir()
    lw_files.clear()
    files = filter(os.listdir(workdir), ext)
    for file in files:
        lw_files.addItem(file)

btn_dir.clicked.connect(showlistimage)

class ImageProcessor:
    def __init__(self):
        self.image = None
        self.filename = None
        self.save_dir = "Modified/"

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)


    def show_image(self):
        lb_image.hide()
        pixmapimage = QPixmap(os.path.join(workdir, self.save_dir, self.filename))
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

workimage = ImageProcessor()

def show():
    if lw_files.currentRow() >=0:
        filename= lw_files.currentItem().text()
        workimage.load_image(filename)
        workimage.show_image()
lw_files.currentRowChanged.connect(show)
win.show()
app.exec_()

