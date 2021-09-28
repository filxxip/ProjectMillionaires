class Question(object):
    def __init__(self, power, contents, answers ):
        self.__power = self.__contents = self.__answers = None
        self.set_power(power)
        self.set_contents(contents)
        self.set_answers(answers)
    def set_power(self,power):
        if self.__validate_power(power):
            self.__power = power
    def set_contents(self, contents):
        self.__contents = contents
    def set_answers(self, answers):
        if self.__validate_answers(answers):
            self.__answers = answers
    def __validate_power(self, power):
        if power in (1, 2, 3):
            return True
        return False
    def __validate_answers(self, answers):
        if len(answers) == 4:
            return True
        return False
    def get_contents(self):
        return self.__contents
    def get_power(self):
        return self.__power
    def get_answers(self):
        return self.__answers
    