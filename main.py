from sqlite3 import Error
from PyQt5 import QtWidgets

from model.question import Question
from model.user import User
from py_ui.start_page import Ui_MainWindow
from py_ui.leaderboard_page import Ui_MainWindow as Ui_leader
from py_ui.main_page import Ui_Quiz as Ui_Main
from db import db_helper as d
import sys
import requests
import html

questions = []


def call_api(level):
    parameters = {
        "amount": 10,
        "type": "multiple",
        "category": 18,
        "difficulty": level
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    question_data = response.json()["results"]
    for i in question_data:
        questions.append(Question(i['question'], i['correct_answer'], i['incorrect_answers']))


class LeadersPage(QtWidgets.QMainWindow, Ui_leader):
    def __init__(self, parent=None):
        super(LeadersPage, self).__init__(parent)
        self.setupUi(self)
        self.newGame.clicked.connect(self.restart)

    def restart(self):
        questions.clear()
        self.main_page = StartPage()
        self.main_page.show()
        self.close()


class MainPage(QtWidgets.QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.i = 0
        self.correct_answers = 0
        self.setupUi(self)
        self.create_question()
        self.lbl_score.setText("0")
        self.odg1.clicked.connect(self.check)
        self.odg2.clicked.connect(self.check)
        self.odg3.clicked.connect(self.check)
        self.odg4.clicked.connect(self.check)
        self.btn_next.clicked.connect(self.on_next_btn)
        self.user_data()

    def create_question(self):
        self.pitanje.setText(html.unescape(questions[self.i].get_question()))
        li = questions[self.i].all_choices()
        self.odg1.setText(html.unescape(li[0]))
        self.odg2.setText(html.unescape(li[1]))
        self.odg3.setText(html.unescape(li[2]))
        self.odg4.setText(html.unescape(li[3]))

    def on_next_btn(self):
        if int(self.i) == int(len(questions) - 1):
            self.lbl_score.setText(str(self.correct_answers))
            conn = d.create_connection()
            with conn:
                try:
                    a = d.select_user(conn)
                    d.update_user(conn, (self.correct_answers, a[0]))
                except Error as e:
                    print(e)
            self.main_page = LeadersPage()
            self.main_page.show()
            self.close()
        else:
            self.i += 1
            self.create_question()
            self.lbl_score.setText(str(self.correct_answers))

    def check(self):
        if self.odg1.isChecked():
            if self.odg1.text() == questions[self.i].get_answers():
                self.correct_answers += 1

        elif self.odg2.isChecked():
            if self.odg2.text() == questions[self.i].get_answers():
                self.correct_answers += 1

        elif self.odg3.isChecked():
            if self.odg3.text() == questions[self.i].get_answers():
                self.correct_answers += 1

        elif self.odg4.isChecked():
            if self.odg4.text() == questions[self.i].get_answers():
                self.correct_answers += 1

    def user_data(self):
        conn = d.create_connection()
        with conn:
            try:
                a = d.select_user(conn)
                user = User(a[0], a[1], a[2], a[3])
                self.lbl_username.setText(user.get_username())
                self.lbl_level.setText(user.get_level().upper())
            except Error as e:
                print(e)


class StartPage(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(StartPage, self).__init__(parent)
        self.setupUi(self)
        self.level.addItems(["Easy", "Medium", "Hard"])
        self.start.clicked.connect(self.get_data)

    def get_data(self):
        level = str(self.level.currentText()).lower()
        username = str(self.username.text()).lower()
        call_api(level)
        conn = d.create_connection()
        with conn:
            try:
                d.create_table(conn)
                user = (username, level)
                d.insert_user(conn, user)
            except Error as e:
                print(e)
        self.main_page = MainPage()
        self.main_page.show()
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = StartPage()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
