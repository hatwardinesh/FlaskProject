from flask import Flask
from flask import request
import logging


app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods =['GET', 'POST'])
def logingex():
    try:
        name = request.args.get('name')
        app.logger.info('you are inside the logger method {}'.format(name))
        return 'Success {}'.format(name)
    except ValueError:    
        return "Error in value"

@app.route('/login')
def login():
    return "Login Success"

@app.route('/login')
def login2():
    app.logger.info('you are inside the logging2  method' )
    return "Login succes in othe method"    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
