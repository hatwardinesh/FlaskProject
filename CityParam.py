from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def getCity():
    city= request.args.get('city')
    return city


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')

