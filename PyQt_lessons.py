## Source: https://github.com/kenwaldek/pythonprogramming/blob/pythonprogramming/pyqt5_lesson_03.py
# Ethan Piper
# July, 2020

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

# import sys
# import PyQt5.QtCore
# from PyQt5.QtCore import QCoreApplication
# # from PyQt5.QtGui import *
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QCheckBox
# from PyQt5.uic.properties import QtGui

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

# import sys
# from PyQt5.QtCore import QCoreApplication, Qt
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
# from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory
#
# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50,50, 500, 300)
#         self.setWindowTitle('lesson 10')
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
#         self.btn.clicked.connect(self.download)
#
#         # create a dropdown for style selection
#         self.styleChoice = QLabel("windowsvista", self)
#         self.styleChoice.move(0, 150)
#
#         # create the combobox and add options
#         comboBox = QComboBox(self)
#         comboBox.addItem('windowsvista')
#         comboBox.addItem('windows')
#         comboBox.addItem('fusion')
#         comboBox.move(25, 250)
#         self.styleChoice.move(25, 150)
#         comboBox.activated[str].connect(self.style_choice)
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
#     def style_choice(self, text):
#         # change the actual style
#         self.styleChoice.setText(text)
#         QApplication.setStyle(QStyleFactory.create(text))
#
# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())
#
# run()

## Lesson 11

## Lesson 12
# import sys
# from PyQt5.QtCore import QCoreApplication, Qt
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
# from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QFontDialog, QColorDialog, QCalendarWidget
#
# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50,50, 500, 300)
#         self.setWindowTitle('lesson 11')
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
#         self.home()
#
#     def home(self):
#         # create "quit" button
#         btn = QPushButton('quit', self)
#         btn.clicked.connect(self.close_application)
#         btn.resize(btn.sizeHint())
#         btn.move(20, 100)
#
#         # create checkbox
#         checkBox = QCheckBox('quadruple the size', self)
#         checkBox.setGeometry(200, 160, 200, 20)
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
#         self.btn.clicked.connect(self.download)
#
#         # create a dropdown for style selection
#         self.styleChoice = QLabel("windowsvista", self)
#         self.styleChoice.move(25, 150)
#
#         # create the combobox and add options
#         comboBox = QComboBox(self)
#         comboBox.addItem('windowsvista')
#         comboBox.addItem('windows')
#         comboBox.addItem('fusion')
#         comboBox.setGeometry(20, 250, 100, 40)
#         self.styleChoice.move(20, 150)
#         comboBox.activated[str].connect(self.style_choice)
#
#         # create a toolbar item
#         extractAction = QAction(QIcon('in_rainbows.jpg'), '2007', self)
#         extractAction.triggered.connect(self.close_application)
#
#         # create the toolbar itself (it will be underneath the menu bar)
#         self.toolBar = self.addToolBar('Extraction')
#         self.toolBar.addAction(extractAction)
#
#         # create a font widget for the toolbar
#         fontPicker = QAction('Font', self)
#         fontPicker.triggered.connect(self.font_picker)
#         # self.toolBar = self.addToolBar('Font')
#         self.toolBar.addAction(fontPicker)
#
#         # add a color-picker widget to the toolbar
#         colorPicker = QAction('Font bg Color', self)
#         colorPicker.triggered.connect(self.color_picker)
#         self.toolBar.addAction(colorPicker)
#
#         # create a calendar
#         calendar = QCalendarWidget(self)
#         calendar.move(200, 200)
#         calendar.resize(300, 300)
#
#         self.show()
#
#     # method for closing the application and printing corresponding messages
#     def close_application(self):
#
#         choice = QMessageBox.question(self, 'Message',
#                                          "Do you actually want to do that? Seriously?", QMessageBox.Yes |
#                                          QMessageBox.No, QMessageBox.Yes)
#
#         if choice == QMessageBox.Yes:
#             print('game OVER')
#             sys.exit()
#         else:
#             pass
#
#     # method for changing the window size depending on the status of a check box
#     def enlarge_window(self,state):
#         if state == Qt.Checked:
#             self.setGeometry(50, 50, 1000, 600)
#         else:
#             self.setGeometry(50,50, 500, 300)
#
#     # method for controlling the status of the download bar
#     def download(self):
#         self.completed = 0
#
#         while self.completed < 100:
#             self.completed += 0.001
#             self.progress.setValue(self.completed)
#
#     # method for selecting the style of the entire page
#     def style_choice(self, text):
#         # change the actual style
#         self.styleChoice.setText(text)
#         QApplication.setStyle(QStyleFactory.create(text))
#
#     # method for font selection
#     def font_picker(self):
#         font, valid = QFontDialog.getFont()
#         if valid:
#             self.styleChoice.setFont(font)
#
#     # method for color selection
#     def color_picker(self):
#         color = QColorDialog.getColor()
#         self.styleChoice.setStyleSheet('QWidget {background-color: %s}' % color.name())
#
# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())
#
# run()

# Lesson 13

# import sys
# from PyQt5.QtCore import QCoreApplication, Qt
# from PyQt5.QtGui import QIcon
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QTextEdit
# from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QFontDialog, QColorDialog, QCalendarWidget
#
# class window(QMainWindow):
#
#     def __init__(self):
#         super(window, self).__init__()
#         self.setGeometry(50,50, 500, 300)
#         self.setWindowTitle('lesson 13')
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
#         # create a text editor widget
#         textEditor = QAction('&Editor', self)
#         textEditor.setShortcut('Ctrl+E')
#         textEditor.setStatusTip('Open Editor')
#         textEditor.triggered.connect(self.text_editor)
#
#         # add the text editor widget to the main menu
#         editorMenu = mainMenu.addMenu('&Editor')
#         editorMenu.addAction(textEditor)
#
#         self.home()
#
#     def home(self):
#         # create "quit" button
#         btn = QPushButton('quit', self)
#         btn.clicked.connect(self.close_application)
#         btn.resize(btn.sizeHint())
#         btn.move(20, 100)
#
#         # create checkbox
#         checkBox = QCheckBox('quadruple the size', self)
#         checkBox.setGeometry(200, 160, 200, 20)
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
#         self.btn.clicked.connect(self.download)
#
#         # create a dropdown for style selection
#         self.styleChoice = QLabel("windowsvista", self)
#         self.styleChoice.move(25, 150)
#
#         # create the combobox and add options
#         comboBox = QComboBox(self)
#         comboBox.addItem('windowsvista')
#         comboBox.addItem('windows')
#         comboBox.addItem('fusion')
#         comboBox.setGeometry(20, 250, 100, 40)
#         self.styleChoice.move(20, 150)
#         comboBox.activated[str].connect(self.style_choice)
#
#         # create a toolbar item
#         extractAction = QAction(QIcon('in_rainbows.jpg'), '2007', self)
#         extractAction.triggered.connect(self.close_application)
#
#         # create the toolbar itself (it will be underneath the menu bar)
#         self.toolBar = self.addToolBar('Extraction')
#         self.toolBar.addAction(extractAction)
#
#         # create a font widget for the toolbar
#         fontPicker = QAction('Font', self)
#         fontPicker.triggered.connect(self.font_picker)
#         # self.toolBar = self.addToolBar('Font')
#         self.toolBar.addAction(fontPicker)
#
#         # add a color-picker widget to the toolbar
#         colorPicker = QAction('Font bg Color', self)
#         colorPicker.triggered.connect(self.color_picker)
#         self.toolBar.addAction(colorPicker)
#
#         # create a calendar
#         calendar = QCalendarWidget(self)
#         calendar.move(200, 200)
#         calendar.resize(300, 300)
#
#         self.show()
#
#     # method for closing the application and printing corresponding messages
#     def close_application(self):
#
#         choice = QMessageBox.question(self, 'Message',
#                                          "Do you actually want to do that? Seriously?", QMessageBox.Yes |
#                                          QMessageBox.No, QMessageBox.Yes)
#
#         if choice == QMessageBox.Yes:
#             print('game OVER')
#             sys.exit()
#         else:
#             pass
#
#     # method for changing the window size depending on the status of a check box
#     def enlarge_window(self,state):
#         if state == Qt.Checked:
#             self.setGeometry(50, 50, 1000, 600)
#         else:
#             self.setGeometry(50,50, 500, 300)
#
#     # method for controlling the status of the download bar
#     def download(self):
#         self.completed = 0
#
#         while self.completed < 100:
#             self.completed += 0.001
#             self.progress.setValue(self.completed)
#
#     # method for selecting the style of the entire page
#     def style_choice(self, text):
#         # change the actual style
#         self.styleChoice.setText(text)
#         QApplication.setStyle(QStyleFactory.create(text))
#
#     # method for font selection
#     def font_picker(self):
#         font, valid = QFontDialog.getFont()
#         if valid:
#             self.styleChoice.setFont(font)
#
#     # method for color selection
#     def color_picker(self):
#         color = QColorDialog.getColor()
#         self.styleChoice.setStyleSheet('QWidget {background-color: %s}' % color.name())
#
#     # method for creating text editor if the corresponding toolbar item is selected
#     def text_editor(self):
#         self.textEdit = QTextEdit()
#         self.setCentralWidget(self.textEdit)
#
# def run():
#     app = QApplication(sys.argv)
#     Gui = window()
#     sys.exit(app.exec_())
#
# run()

# Lesson 14 / 15

import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox, QTextEdit, QFileDialog
from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QFontDialog, QColorDialog, QCalendarWidget

name = "" # global variable for keeping track of the name of the file that is open.

class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50,50, 500, 300)
        self.setWindowTitle('lesson 15')

        # create an item to be put into the menu
        extractAction = QAction('woohoo', self)
        extractAction.setShortcut('ctrl+d')
        extractAction.setStatusTip('leave the app')
        extractAction.triggered.connect(self.close_application)

        # create the menu bar itself
        mainMenu = self.menuBar()

        # create the file menu and add "Quit" to it
        fileMenu = mainMenu.addMenu('File')
        fileMenu.addAction(extractAction)

        # create a text editor widget
        textEditor = QAction('&Editor', self)
        textEditor.setShortcut('Ctrl+E')
        textEditor.setStatusTip('Open Editor')
        textEditor.triggered.connect(self.text_editor)

        # add the text editor widget to the main menu
        editorMenu = mainMenu.addMenu('&Editor')
        editorMenu.addAction(textEditor)

        # create a file-access widget
        openFile = QAction("&Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open')
        openFile.triggered.connect(self.open_file)

        # add the file-access widget to the file menu
        fileMenu.addAction(openFile)

        # create a file-save-as widget
        saveAsFile = QAction('&Save As', self)
        saveAsFile.setStatusTip('Save As')
        saveAsFile.triggered.connect(self.save_as_file)

        # create a regular save widget
        saveFile = QAction('&Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save')
        saveFile.triggered.connect(self.save_file)

        # add the file-save widgets to the file menu
        fileMenu.addAction(saveAsFile)
        fileMenu.addAction(saveFile)

        # display the relevant information in the status bar
        self.statusBar()

        self.home()

    def home(self):
        # create "quit" button
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(20, 100)

        # create checkbox
        checkBox = QCheckBox('quadruple the size', self)
        checkBox.setGeometry(200, 160, 200, 20)
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
        self.styleChoice.move(25, 150)

        # create the combobox and add options
        comboBox = QComboBox(self)
        comboBox.addItem('windowsvista')
        comboBox.addItem('windows')
        comboBox.addItem('fusion')
        comboBox.setGeometry(20, 250, 100, 40)
        self.styleChoice.move(20, 150)
        comboBox.activated[str].connect(self.style_choice)

        # create a toolbar item
        extractAction = QAction(QIcon('in_rainbows.jpg'), '2007', self)
        extractAction.triggered.connect(self.close_application)

        # create the toolbar itself (it will be underneath the menu bar)
        self.toolBar = self.addToolBar('Toolbar 1')
        self.toolBar.addAction(extractAction)

        # create a font widget for the toolbar
        fontPicker = QAction('Font', self)
        fontPicker.triggered.connect(self.font_picker)
        # self.toolBar = self.addToolBar('Font')
        self.toolBar.addAction(fontPicker)

        # add a color-picker widget to the toolbar
        colorPicker = QAction('Font bg Color', self)
        colorPicker.triggered.connect(self.color_picker)
        self.toolBar.addAction(colorPicker)

        # create a calendar
        calendar = QCalendarWidget(self)
        calendar.move(200, 200)
        calendar.resize(300, 300)

        self.show()

    # method for closing the application and printing corresponding messages
    def close_application(self):

        choice = QMessageBox.question(self, 'Message',
                                         "Do you actually want to do that? Seriously?", QMessageBox.Yes |
                                         QMessageBox.No, QMessageBox.Yes)

        if choice == QMessageBox.Yes:
            print('game OVER')
            sys.exit()
        else:
            pass

    # method for changing the window size depending on the status of a check box
    def enlarge_window(self,state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50,50, 500, 300)

    # method for controlling the status of the download bar
    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.001
            self.progress.setValue(self.completed)

    # method for selecting the style of the entire page
    def style_choice(self, text):
        # change the actual style
        self.styleChoice.setText(text)
        QApplication.setStyle(QStyleFactory.create(text))

    # method for font selection
    def font_picker(self):
        font, valid = QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)

    # method for color selection
    def color_picker(self):
        color = QColorDialog.getColor()
        self.styleChoice.setStyleSheet('QWidget {background-color: %s}' % color.name())

    # method for creating text editor if the corresponding toolbar item is selected
    def text_editor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

    # method for opening files
    def open_file(self):
        global name
        name = "" # reset the name of the file opened because we are opening a new file now. 
        name, _ = QFileDialog.getOpenFileName(self, 'Open File')

        # check that the file was properly opened.
        if name:
            file = open(name, 'r')

            self.text_editor()

            with file:
                text = file.read()
                self.textEdit.setText(text)

    # method for saving files (must select file name and storage location)
    def save_as_file(self):
        # save_as_file is NOT the same as the global variable "name"
        save_as_name, _ = QFileDialog.getSaveFileName(self, 'Save File')

        # check that the file was properly opened
        if save_as_name:
            file = open(save_as_name, 'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()

    # method for saving files (must select file name and storage location)
    def save_file(self):
        # access the file that is currently opened. If one is currently opened. Otherwise, call save_as_file.
        global name

        # check that the file was properly opened
        if (name):
            file = open(name, 'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()
        else:
            self.save_as_file()


def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()
