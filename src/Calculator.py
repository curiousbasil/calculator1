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

def sqrt (a):
    return a ** 0.5


class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result= x;
        pass

    def add(self, a, b):
        a = float(a)
        b = float(b)
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        a = float(a)
        b = float(b)
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        a = float(a)
        b = float(b)
        self.result = division(a, b)
        return self.result

    def squared(self, a, ):
        a = float(a)
        self.result = squared(a)
        return self.result

    def sqrt(self, a, ):
        a = float(a)
        self.result = sqrt(a)
        return self.result