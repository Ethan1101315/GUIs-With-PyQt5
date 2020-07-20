## Source: https://github.com/kenwaldek/pythonprogramming/blob/pythonprogramming/pyqt5_lesson_03.py

## lesson 3
# import sys
# from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
#
#
# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50, 50, 500, 300)
#         self.setWindowTitle('pyqt5 Tut')
#         self.setWindowIcon(QIcon('pic.png'))
#         self.home()
#
#     def home(self):
#         btn = QPushButton('quit', self)
#         btn.clicked.connect(QCoreApplication.instance().quit)
#         btn.resize(100,100)
#         btn.move(100,00)
#         self.show()
#
# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())
#
# run()

## lesson 4

# import sys
# from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
#
#
# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50, 50, 500, 300)
#         self.setWindowTitle("PyQt Tutorial")
#         self.setWindowIcon(QIcon('pythonlogo.png'))
#         self.home()
#
#     def home(self):
#         btn = QPushButton("Quit", self)
#         btn.clicked.connect(self.close_application)
#         btn.resize(btn.sizeHint())
#         btn.move(0,0)
#         self.show()
#
#     def close_application(self):
#         print("Yankee Hotel Foxtrot")
#         sys.exit()
#
# def run():
#     app = QApplication(sys.argv)
#     GUI = window()
#     sys.exit(app.exec_())
#
# run()

## lesson 5
