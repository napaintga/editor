
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
btn_bw = QPushButton("Чорно-білий")
btn_left = QPushButton("Ліво")
btn_right = QPushButton("Право")
btn_flip =QPushButton('Відзеркалити')
btn_sharp = QPushButton('Різкість')
btn_blur = QPushButton('бЛЮР')
_23yu= "12"


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
row.addWidget(btn_bw)
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
        self.save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Modified/")

    def do_bw(self):
        self.image = self.image.convert("L")
        self.save_image()
    def do_90(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
    def do_270(self):
        self.image= self.image.transpose(Image.ROTATE_270)
        self.save_image()
        
    def do_flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
    def do_sahp(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        
    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(workdir, filename)
        self.image = Image.open(fullname)

    def save_image(self):
        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)
        image_path = os.path.join(self.save_dir, self.filename)
        self.image.save(image_path)
        self.show_image(image_path)
            
    def show_image(self,path):
        lb_image.hide()
        pixmapimage = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        lb_image.setPixmap(pixmapimage)
        lb_image.show()

workimage = ImageProcessor()

def show():
    filename= lw_files.currentItem().text()
    workimage.load_image(filename)
    full_path = os.path.join(workdir,filename)
    workimage.show_image(full_path)
    
lw_files.currentRowChanged.connect(show)
btn_left.clicked.connect(workimage.do_90)
btn_right.clicked.connect(workimage.do_270)
btn_flip.clicked.connect(workimage.do_flip)
btn_blur.clicked.connect(workimage.do_blur)
btn_bw.clicked.connect(workimage.do_bw)
btn_sharp.clicked.connect(workimage.do_sahp)
win.resize(600,550)

win.show()
app.exec_()

