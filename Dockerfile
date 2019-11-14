FROM python:3.7

ADD . .

CMD [ "python" , "./src/CalculatorTests.py" ]