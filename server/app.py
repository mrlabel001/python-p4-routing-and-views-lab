#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return string

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = list(range(parameter))
    result = ''
    for num in numbers:
        result += '{}\n'.format(num)
    return result

@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = ''

    if operation == '+':
        result = '{} + {} = {}'.format(num1, num2, num1 + num2)
    elif operation == '-':
        result = '{} - {} = {}'.format(num1, num2, num1 - num2)
    elif operation == '*':
        result = '{} * {} = {}'.format(num1, num2, num1 * num2)
    elif operation == 'div':
        if num2 != 0:
            result = '{} / {} = {}'.format(num1, num2, num1 / num2)
        else:
            result = 'Error: Division by zero'
    elif operation == '%':
        result = '{} % {} = {}'.format(num1, num2, num1 % num2)
    else:
        result = 'Invalid operation'

    return result

if __name__ == '__main__':
    app.run(port=5555, debug=True)
