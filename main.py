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
        self.top10()

    def restart(self):
        questions.clear()
        self.main_page = StartPage()
        self.main_page.show()
        self.close()

    def top10(self):
        conn = d.create_connection()
        with conn:
            try:
                easy = d.select_top10_users(conn, "easy")
                medium = d.select_top10_users(conn, "medium")
                hard = d.select_top10_users(conn, "hard")

                self.easyRank(easy)
                self.mediumRank(medium)
                self.hardRank(hard)
            except Error as e:
                print(e)

    def easyRank(self, easy):
        try:
            self.user_easy_1.setText(easy[0][0])
            self.score_easy_1.setText(str(easy[0][1]))
        except IndexError:
            self.user_easy_1.setText("")
            self.score_easy_1.setText(str(""))

        try:
            self.user_easy_2.setText(easy[1][0])
            self.score_easy_2.setText(str(easy[1][1]))
        except IndexError:
            self.user_easy_2.setText("")
            self.score_easy_2.setText(str(""))

        try:
            self.user_easy_3.setText(easy[2][0])
            self.score_easy_3.setText(str(easy[2][1]))
        except IndexError:
            self.user_easy_3.setText("")
            self.score_easy_3.setText(str(""))

        try:
            self.user_easy_4.setText(easy[3][0])
            self.score_easy_4.setText(str(easy[3][1]))
        except IndexError:
            self.user_easy_4.setText("")
            self.score_easy_4.setText(str(""))

        try:
            self.user_easy_5.setText(easy[4][0])
            self.score_easy_5.setText(str(easy[4][1]))
        except IndexError:
            self.user_easy_5.setText("")
            self.score_easy_5.setText(str(""))

        try:
            self.user_easy_6.setText(easy[5][0])
            self.score_easy_6.setText(str(easy[5][1]))
        except IndexError:
            self.user_easy_6.setText("")
            self.score_easy_6.setText(str(""))

        try:
            self.user_easy_7.setText(easy[6][0])
            self.score_easy_7.setText(str(easy[6][1]))
        except IndexError:
            self.user_easy_7.setText("")
            self.score_easy_7.setText(str(""))

        try:
            self.user_easy_8.setText(easy[7][0])
            self.score_easy_8.setText(str(easy[7][1]))
        except IndexError:
            self.user_easy_8.setText("")
            self.score_easy_8.setText(str(""))

        try:
            self.user_easy_9.setText(easy[8][0])
            self.score_easy_9.setText(str(easy[8][1]))
        except IndexError:
            self.user_easy_9.setText("")
            self.score_easy_9.setText(str(""))

        try:
            self.user_easy_10.setText(easy[9][0])
            self.user_easy_10.setText(str(easy[9][1]))
        except IndexError:
            self.user_easy_10.setText("")
            self.user_easy_10.setText(str(""))

    def mediumRank(self, medium):
        try:
            self.user_med_1.setText(medium[0][0])
            self.score_med_1.setText(str(medium[0][1]))
        except IndexError:
            self.user_med_1.setText("")
            self.score_med_1.setText(str(""))

        try:
            self.user_med_2.setText(medium[1][0])
            self.score_med_2.setText(str(medium[1][1]))
        except IndexError:
            self.user_med_2.setText("")
            self.score_med_2.setText(str(""))

        try:
            self.user_med_3.setText(medium[2][0])
            self.score_med_3.setText(str(medium[2][1]))
        except IndexError:
            self.user_med_3.setText("")
            self.score_med_3.setText(str(""))

        try:
            self.user_med_4.setText(medium[3][0])
            self.score_med4.setText(str(medium[3][1]))
        except IndexError:
            self.user_med_4.setText("")
            self.score_med4.setText(str(""))

        try:
            self.user_med_5.setText(medium[4][0])
            self.score_med_5.setText(str(medium[4][1]))
        except IndexError:
            self.user_med_5.setText("")
            self.score_med_5.setText(str(""))

        try:
            self.user_med_6.setText(medium[5][0])
            self.score_med_6.setText(str(medium[5][1]))
        except IndexError:
            self.user_med_6.setText("")
            self.score_med_6.setText(str(""))

        try:
            self.user_med_7.setText(medium[6][0])
            self.score_med_7.setText(str(medium[6][1]))
        except IndexError:
            self.user_med_7.setText("")
            self.score_med_7.setText(str(""))

        try:
            self.user_med_8.setText(medium[7][0])
            self.score_med_8.setText(str(medium[7][1]))
        except IndexError:
            self.user_med_8.setText("")
            self.score_med_8.setText(str(""))

        try:
            self.user_med_9.setText(medium[8][0])
            self.score_med_9.setText(str(medium[8][1]))
        except IndexError:
            self.user_med_9.setText("")
            self.score_med_9.setText(str(""))

        try:
            self.user_med_10.setText(medium[9][0])
            self.score_med_10.setText(str(medium[9][1]))
        except IndexError:
            self.user_med_10.setText("")
            self.score_med_10.setText(str(""))

    def hardRank(self, hard):
        try:
            self.user_hard_1.setText(hard[0][0])
            self.score_hard_1.setText(str(hard[0][1]))
        except IndexError:
            self.user_hard_1.setText("")
            self.score_hard_1.setText(str(""))

        try:
            self.user_hard_2.setText(hard[1][0])
            self.score_hard_2.setText(str(hard[1][1]))
        except IndexError:
            self.user_hard_2.setText("")
            self.score_hard_2.setText(str(""))

        try:
            self.user_hard_3.setText(hard[2][0])
            self.score_hard_3.setText(str(hard[2][1]))
        except IndexError:
            self.user_hard_3.setText("")
            self.score_hard_3.setText(str(""))

        try:
            self.user_hard_4.setText(hard[3][0])
            self.score_hard_4.setText(str(hard[3][1]))
        except IndexError:
            self.user_hard_4.setText("")
            self.score_hard_4.setText(str(""))

        try:
            self.user_hard_5.setText(hard[4][0])
            self.score_hard_5.setText(str(hard[4][1]))
        except IndexError:
            self.user_hard_5.setText("")
            self.score_hard_5.setText(str(""))

        try:
            self.user_hard_6.setText(hard[5][0])
            self.score_hard_6.setText(str(hard[5][1]))
        except IndexError:
            self.user_hard_6.setText("")
            self.score_hard_6.setText(str(""))

        try:
            self.user_hard_7.setText(hard[6][0])
            self.score_hard_7.setText(str(hard[6][1]))
        except IndexError:
            self.user_hard_7.setText("")
            self.score_hard_7.setText(str(""))

        try:
            self.user_hard_8.setText(hard[7][0])
            self.score_hard_8.setText(str(hard[7][1]))
        except IndexError:
            self.user_hard_8.setText("")
            self.score_hard_8.setText(str(""))

        try:
            self.user_hard_9.setText(hard[8][0])
            self.score_hard_9.setText(str(hard[8][1]))
        except IndexError:
            self.user_hard_9.setText("")
            self.score_hard_9.setText(str(""))

        try:
            self.user_hard_10.setText(hard[9][0])
            self.score_hard_10.setText(str(hard[9][1]))
        except IndexError:
            self.user_hard_10.setText("")
            self.score_hard_10.setText(str(""))


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

        self.odg1.setAutoExclusive(False)
        self.odg2.setAutoExclusive(False)
        self.odg3.setAutoExclusive(False)
        self.odg4.setAutoExclusive(False)

        self.odg1.setChecked(False)
        self.odg2.setChecked(False)
        self.odg3.setChecked(False)
        self.odg4.setChecked(False)

        self.odg1.setAutoExclusive(True)
        self.odg2.setAutoExclusive(True)
        self.odg3.setAutoExclusive(True)
        self.odg4.setAutoExclusive(True)

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
