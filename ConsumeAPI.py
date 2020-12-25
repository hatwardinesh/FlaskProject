from flask import Flask
import requests 

app= Flask(__name__)

@app.route('/')
def callAPI():
    text= (requests.get('https://reqres.in/api/users/2')).json()
   
    print(text)
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')    