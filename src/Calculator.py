def addition (a, b):
    return a + b

def subtraction (a, b):
    return a - b

def multiplication (a, b):
    return a * b

def division (a, b):
    return a / b


class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result= x;
        pass

    def add(self, a, b):
        self.result = a + b
        return addition(a, b)


