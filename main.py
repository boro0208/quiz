from sqlite3 import Error
from PyQt5 import QtWidgets
from py_ui.start_page import Ui_MainWindow
from py_ui.main_page import Ui_MainWindow as Ui_Main
from db import db_helper as d
import sys
import requests


def call_api(level):
    parameters = {
        "amount": 10,
        "type": "multiple",
        "category": 18,
        "difficulty": level
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    question_data = response.json()["results"]
    print(question_data)


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
        call_api(level)


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = StartPage()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
