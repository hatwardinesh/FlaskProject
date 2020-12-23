from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/cal' , methods=['GET', 'POST'])
def calculate():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        return str(a+b)
    except ValueError:
        return "Please enter numeric values only"
if __name__  == "__main__":
    app.run(app.run(host='0.0.0.0', port=8080))   