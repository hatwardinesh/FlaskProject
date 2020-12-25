from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def postApiCall():
    name= request.args.get('name')
    city = request.args.get('city')
    print('name : {} and city : {}'.format(name,city))
    return "Success"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= '8080')    

