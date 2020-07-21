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

# import sys
# from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import *
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QAction
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
#
#
# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50, 50, 500, 300)
#         self.setWindowTitle('pyqt5 Tut')
#         # self.setWindowIcon(QIcon('pic.png'))
#
#         extractAction = QAction('yeehaw', self)
#         extractAction.setShortcut('Ctrl+Q')
#         extractAction.setStatusTip('close app')
#         extractAction.triggered.connect(self.close_application)
#
#         self.statusBar()
#
#         mainMenu = self.menuBar()
#         fileMenu = mainMenu.addMenu('&File')
#         fileMenu.addAction(extractAction)
#
#         self.home()
#
#     def home(self):
#         btn = QPushButton('quit', self)
#         btn.clicked.connect(self.close_application)
#
#         btn.resize(btn.sizeHint())
#         btn.move(0, 100)
#         self.show()
#
#     def close_application(self):
#         print('whooo so custom')
#         sys.exit()
#
# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())
#
# run()

## lesson 6

# import sys
# from PyQt5.QtCore import QCoreApplication
# # from PyQt5.QtGui import *
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction
# from PyQt5.uic.properties import QtGui
#
# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50,50, 500, 300)
#         self.setWindowTitle('lesson 6')
#
#         extractAction = QAction('woohoo', self)
#         extractAction.setShortcut('ctrl+d')
#         extractAction.setStatusTip('leave the app')
#         extractAction.triggered.connect(self.close_application)
#
#         self.statusBar()
#
#         mainMenu = self.menuBar()
#         fileMenu = mainMenu.addMenu('Click here')
#         fileMenu.addAction(extractAction)
#
#         extractAction = QAction(QIcon('in_rainbows.jpg'), '2007', self)
#         extractAction.triggered.connect(self.close_application)
#
#         self.toolBar = self.addToolBar('Extraction')
#         self.toolBar.addAction(extractAction)
#
#         self.home()
#
#     def home(self):
#         btn = QPushButton('quit', self)
#         btn.clicked.connect(self.close_application)
#         btn.resize(btn.sizeHint())
#         btn.move(0, 100)
#
#         self.show()
#
#     def close_application(self):
#         print('baaah')
#         sys.exit()
#
# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())
#
# run()

## lesson 7

# import sys
# from PyQt5.QtCore import QCoreApplication
# # from PyQt5.QtGui import *
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
# from PyQt5.uic.properties import QtGui
#
# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50,50, 500, 300)
#         self.setWindowTitle('lesson 6')
#
#         extractAction = QAction('woohoo', self)
#         extractAction.setShortcut('ctrl+d')
#         extractAction.setStatusTip('leave the app')
#         extractAction.triggered.connect(self.close_application)
#
#         self.statusBar()
#
#         mainMenu = self.menuBar()
#         fileMenu = mainMenu.addMenu('Click here')
#         fileMenu.addAction(extractAction)
#
#         extractAction = QAction(QIcon('in_rainbows.jpg'), '2007', self)
#         extractAction.triggered.connect(self.close_application)
#
#         self.toolBar = self.addToolBar('Extraction')
#         self.toolBar.addAction(extractAction)
#
#         self.home()
#
#     def home(self):
#         btn = QPushButton('quit', self)
#         btn.clicked.connect(self.close_application)
#         btn.resize(btn.sizeHint())
#         btn.move(0, 100)
#
#         self.show()
#
#     def close_application(self):
#
#         choice = QMessageBox.question(self, 'Message',
#                                          "Do you actually want to do that? Seriously?", QMessageBox.Yes |
#                                          QMessageBox.No, QMessageBox.Yes)
#
#         if choice == QMessageBox.Yes:
#             print('quit application')
#             sys.exit()
#         else:
#             pass
#
# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())
#
# run()

## lesson 8

import sys
import PyQt5.QtCore
from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QCheckBox
from PyQt5.uic.properties import QtGui

# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50,50, 500, 300)
#         self.setWindowTitle('lesson 6')
#
#         extractAction = QAction('woohoo', self)
#         extractAction.setShortcut('ctrl+d')
#         extractAction.setStatusTip('leave the app')
#         extractAction.triggered.connect(self.close_application)
#
#         self.statusBar()
#
#         mainMenu = self.menuBar()
#         fileMenu = mainMenu.addMenu('Click here')
#         fileMenu.addAction(extractAction)
#
#         extractAction = QAction(QIcon('in_rainbows.jpg'), '2007', self)
#         extractAction.triggered.connect(self.close_application)
#
#         self.toolBar = self.addToolBar('Extraction')
#         self.toolBar.addAction(extractAction)
#
#         self.home()
#
#     def home(self):
#         btn = QPushButton('quit', self)
#         btn.clicked.connect(self.close_application)
#         btn.resize(btn.sizeHint())
#         btn.move(0, 100)
#
#         checkBox = QCheckBox('quadruple the size', self)
#         checkBox.move(0,50)
#         checkBox.stateChanged.connect(self.enlarge_window)
#
#
#         self.show()
#
#     def close_application(self):
#
#         choice = QMessageBox.question(self, 'Message',
#                                          "Do you actually want to do that? Seriously?", QMessageBox.Yes |
#                                          QMessageBox.No, QMessageBox.Yes)
#
#         if choice == QMessageBox.Yes:
#             print('quit application')
#             sys.exit()
#         else:
#             pass
#
#     def enlarge_window(self,state):
#         if state == PyQt5.QtCore.Qt.Checked:
#             self.setGeometry(50, 50, 1000, 600)
#         else:
#             self.setGeometry(50,50, 500, 300)
#
# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())
#
# run()

## lesson 9

# import sys
# from PyQt5.QtCore import QCoreApplication, Qt
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
# from PyQt5.QtWidgets import QCheckBox, QProgressBar
#
# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50,50, 500, 300)
#         self.setWindowTitle('lesson 6')
#
#         # create an item to be put into the menu
#         extractAction = QAction('woohoo', self)
#         extractAction.setShortcut('ctrl+d')
#         extractAction.setStatusTip('leave the app')
#         extractAction.triggered.connect(self.close_application)
#
#         self.statusBar()
#
#         # create the menu bar itself
#         mainMenu = self.menuBar()
#         fileMenu = mainMenu.addMenu('Click here')
#         fileMenu.addAction(extractAction)
#
#         # create a toolbar item
#         extractAction = QAction(QIcon('in_rainbows.jpg'), '2007', self)
#         extractAction.triggered.connect(self.close_application)
#
#         # create the toolbar itself (it will be underneath the menu bar)
#         self.toolBar = self.addToolBar('Extraction')
#         self.toolBar.addAction(extractAction)
#
#         self.home()
#
#     def home(self):
#         # create "quit" button
#         btn = QPushButton('quit', self)
#         btn.clicked.connect(self.close_application)
#         btn.resize(btn.sizeHint())
#         btn.move(0, 100)
#
#         # create checkbox
#         checkBox = QCheckBox('quadruple the size', self)
#         checkBox.setGeometry(100, 35, 200, 20)
#         #checkBox.move(0,62.5)
#         checkBox.stateChanged.connect(self.enlarge_window)
#
#         # create progress bar
#         self.progress = QProgressBar(self)
#         self.progress.setGeometry(200, 80, 288,20)
#
#         # create button to activate progress bar
#         self.btn = QPushButton('Download self esteem', self)
#         self.btn.setGeometry(200, 120, 250,20)
#
#         #self.btn.move(200, 120)
#         self.btn.clicked.connect(self.download)
#
#         self.show()
#
#     def close_application(self):
#
#         choice = QMessageBox.question(self, 'Message',
#                                          "Do you actually want to do that? Seriously?", QMessageBox.Yes |
#                                          QMessageBox.No, QMessageBox.Yes)
#
#         if choice == QMessageBox.Yes:
#             print('quit application')
#             sys.exit()
#         else:
#             pass
#
#     def enlarge_window(self,state):
#         if state == Qt.Checked:
#             self.setGeometry(50, 50, 1000, 600)
#         else:
#             self.setGeometry(50,50, 500, 300)
#
#     def download(self):
#         self.completed = 0
#
#         while self.completed < 100:
#             self.completed += 0.001
#             self.progress.setValue(self.completed)
#
# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())
#
# run()

## lesson 10

import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50,50, 500, 300)
        self.setWindowTitle('lesson 6')

        # create an item to be put into the menu
        extractAction = QAction('woohoo', self)
        extractAction.setShortcut('ctrl+d')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        # create the menu bar itself
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('Click here')
        fileMenu.addAction(extractAction)

        # create a toolbar item
        extractAction = QAction(QIcon('in_rainbows.jpg'), '2007', self)
        extractAction.triggered.connect(self.close_application)

        # create the toolbar itself (it will be underneath the menu bar)
        self.toolBar = self.addToolBar('Extraction')
        self.toolBar.addAction(extractAction)

        self.home()

    def home(self):
        # create "quit" button
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(0, 100)

        # create checkbox
        checkBox = QCheckBox('quadruple the size', self)
        checkBox.setGeometry(100, 35, 200, 20)
        #checkBox.move(0,62.5)
        checkBox.stateChanged.connect(self.enlarge_window)

        # create progress bar
        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 288,20)

        # create button to activate progress bar
        self.btn = QPushButton('Download self esteem', self)
        self.btn.setGeometry(200, 120, 250,20)
        self.btn.clicked.connect(self.download)

        # create a dropdown for style selection
        self.styleChoice = QLabel("windowsvista", self)
        self.styleChoice.move(0, 150)

        # create the combobox and add options
        comboBox = QComboBox(self)
        comboBox.addItem('windowsvista')
        comboBox.addItem('windows')
        comboBox.addItem('fusion')
        comboBox.move(25, 250)
        self.styleChoice.move(25, 150)
        comboBox.activated[str].connect(self.style_choice)

        self.show()

    def close_application(self):

        choice = QMessageBox.question(self, 'Message',
                                         "Do you actually want to do that? Seriously?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.Yes)

        if choice == QMessageBox.Yes:
            print('quit application')
            sys.exit()
        else:
            pass

    def enlarge_window(self,state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50,50, 500, 300)

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.001
            self.progress.setValue(self.completed)

    def style_choice(self, text):
        # change the actual style
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()
