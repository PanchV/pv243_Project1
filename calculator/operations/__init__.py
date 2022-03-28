""" Operation Classes """

class Addition:
    """ wrapper for addition """

    @staticmethod
    def add(val1, val2):
        """ addition method """
        return val1 + val2


class Subtraction:
    """ wrapper for subtraction """

    @staticmethod
    def subtract(val1, val2):
        """ subtraction method """
        return val1 - val2


class Multiplication:
    """ wrapper for multiplication """

    @staticmethod
    def multiply(val1, val2):
        """ multiplcation method """
        return val1 * val2

class Division:
    @staticmethod
    def divide(val1, val2):
        """ Division method """
        if (val2 == 0):
            return "Divide By Zero Error!"
        else:
            return val1 / val2