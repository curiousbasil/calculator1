def addition (a, b):
    return a + b

def subtraction (a, b):
    return a - b

def multiplication (a, b):
    return a * b

def division (a, b):
    return a / b

def squared (a):
    return a ** 2

class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result= x;
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multipy(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def squared(self, a, ):
        self.result = squared(a)
        return self.result