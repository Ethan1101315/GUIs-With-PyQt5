# basic skeleton code for viewing and adding functionality to windows created using QtDesigner5
# prints to the screen when the pushbutton is clicked. 
# Source for skeleton: https://www.learnpyqt.com/courses/qt-creator/embed-pyqtgraph-custom-widgets-qt-app/
# Source for integrating functionality into the layout: https://www.pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/

from PyQt5 import QtWidgets, uic
import sys

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #Load the UI Page
        uic.loadUi('QtDesigner_test.ui', self)
        self.pushButton.clicked.connect(self.test1)

    def test1(self):
        print("test")

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
