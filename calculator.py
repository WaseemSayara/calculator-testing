
class Calculator:

    @staticmethod
    def addition(first, second):
        try:
            return round(first+second, 10)
        except TypeError:
            print("wrong input entered ( only numbers allowed )")
            return None

    @staticmethod
    def subtraction(first, second):
        try:
            return round(first-second, 10)
        except TypeError:
            print("wrong input entered ( only numbers allowed )")
            return None

    @staticmethod
    def multiply(multiplicand, multiplier):
        if not isinstance(multiplicand, str) and not isinstance(multiplier, str):
            return round(multiplicand*multiplier, 10)
        else:
            return None

    @staticmethod
    def division(first, second):
        try:
            return round(first/second, 10)
        except ZeroDivisionError:
            print("Can't divide on 0 ")
            return None
        except TypeError:
            print("wrong input entered ( only numbers allowed )")
            return None
