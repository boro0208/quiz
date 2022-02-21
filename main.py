from sqlite3 import Error
from PyQt5 import QtWidgets, QtCore, QtGui
from py_ui.start_page import Ui_MainWindow
from py_ui.main_page import Ui_MainWindow as Ui_Main
from db import db_helper as d
import sys


class MainPage(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)


class StartPage(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(StartPage, self).__init__(parent)
        self.setupUi(self)
        self.level.addItems(["Easy", "Medium", "Hard"])
        self.start.clicked.connect(self.get_data)

    def get_data(self):
        level = str(self.level.currentText()).lower()
        username = str(self.username.text()).lower()
        self.main_page = MainPage()
        self.main_page.show()
        self.close()
        conn = d.create_connection()
        with conn:
            try:
                d.create_table(conn)
                user = (username, level)
                d.insert_user(conn, user)
            except Error as e:
                print(e)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = StartPage()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
