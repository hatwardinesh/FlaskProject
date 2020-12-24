from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def retDictionary():
    dictVar = {'a':1, 'b':2, 'c':3}
    return dictVar

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= '8080')    