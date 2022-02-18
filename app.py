from urllib import response
from flask import Flask, render_template, request, jsonify

import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hypotenusePage')
def hypotenuse():
    return render_template('hypotenusePage.html')

@app.route('/hypo', methods=['POST'])
def hypo():
    response = {}
    data = request.get_json( )
    if data.get('base', 'altitude'):
        baseNum = int(data['base'])
        altNum = int(data['altitude'])
        response = {'status': 200, 'result': math.sqrt(baseNum*baseNum + altNum*altNum)}
    else:
        response = {'status': 500, 'result': 'Error'}
    return jsonify(response)

@app.route('/squarerootPage')
def squareRoot():
    return render_template('squarerootPage.html')

@app.route('/squareRoot', methods=['POST'])
def square():
    response = {}
    data = request.get_json( )
    if data.get('number'):
        number = int(data['number'])
        response = {'status': 200, 'result': math.sqrt(number)}
    else:
        response = {'status': 500, 'result': 'Error'}
    return jsonify(response)

@app.route('/scorePage')
def Score():
    return render_template('scorePage.html')

@app.route('/scoreConv', methods=['POST'])
def scoreConv():
    response = {}
    data = request.get_json( )
    if data.get('score'):
        scoreNum = int(data['score'])

        if scoreNum >= 90:
            grade = 'A'
        elif scoreNum >= 80 and scoreNum < 90:
            grade = 'B'
        elif scoreNum >= 70 and scoreNum < 80:
            grade = 'C'
        elif scoreNum >= 60 and scoreNum < 70:
            grade = 'D'
        elif scoreNum < 50:
            grade = 'F'
        response = {'status': 200, 'result': grade}
    else:
        response = {'status': 500, 'result': 'Error'}
    return jsonify(response)