from flask import Flask
from functools import wraps

app = Flask(__name__)

def check_positive(func):  
    @wraps(func)  
    def func_wrapper(x, y):
        try:
            x = int(x)
            y= int(y)
        except ValueError:
            return "Please enter numeric values only"
        
        if x<0 or y<0:
            
            raise Exception("Both x and y have to be positive for function {} to work".format(func.__name__))
        res = func(x,y)
        return res
    return func_wrapper

@app.route('/<x>/<y>')
@check_positive
def addiionOfTwoPositiveNumbers(x,y):
    return str(x+y)




if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host= '0.0.0.0', port='8080')    