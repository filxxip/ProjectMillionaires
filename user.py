class User(object):
    def __init__(self, login, password, games = 0, wins = 0):
        self.__login = self.__password = None
        self.set_login(login)
        self.set_password(password)
        self.__games = games
        self.__wins = wins
    def set_login(self, login):
        self.__login = login
    def set_password(self, password):
        if self.__validate_password(password):
            self.__password = password
    def set_wins(self, wins):
        self.__wins = wins
    def set_games(self, games):
        self.__games = games
    def get_login(self):
        return self.__login
    def get_password(self):
        return self.__password
    def get_games(self):
        return self.__games
    def get_wins(self):
        return self.__wins
    def __validate_password(self, password):
        for x in range(0, len(password)):
            if password[x] == password.upper()[x]:
                return True
        return False
    

