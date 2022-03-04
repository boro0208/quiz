import copy
import random


class Question:
    def __init__(self, question: str, correct_answer: str, choices: list):
        self.__question_text = question
        self.__correct_answer = correct_answer
        self.__choices = choices

    def get_question(self):
        return self.__question_text

    def set_question(self, q):
        self.__question_text = q

    def get_answers(self):
        return self.__correct_answer

    def set_answer(self, q):
        self.__correct_answer = q

    def get_choices(self):
        return self.__choices

    def set_choices(self, q):
        self.__choices = q

    def all_choices(self):
        li = copy.deepcopy(self.__choices)
        li.insert(random.randint(0, len(li)), self.__correct_answer)
        return li
