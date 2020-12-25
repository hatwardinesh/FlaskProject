from flask import Flask
from flask import request
import os

app= Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])
def captureVariables():
    try:
        name= request.args.get('name')
        env = os.environ.get('TEMP')
        return "Hi {} environment path is:  ".format(name) + env
    except ValueError:
        return "provide some name"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')



