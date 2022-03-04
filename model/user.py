class User:
    def __init__(self, id, username, level, score):
        self.__id = id
        self.__username = username
        self.__level = level
        self.__score = score

    def get_id(self):
        return self.__id

    def set_id(self, q):
        self.__id = q

    def get_username(self):
        return self.__username

    def set_username(self, q):
        self.__username = q

    def get_level(self):
        return self.__level

    def set_level(self, q):
        self.__level = q

    def get_score(self):
        return self.__score

    def set_score(self, q):
        self.__score = q
