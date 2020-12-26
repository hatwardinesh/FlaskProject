from flask import Flask
from flask import request
import googletrans
from googletrans import Translator 

app = Flask(__name__)
translator = Translator()

@app.route('/<inputLangString>')
def translateWord(inputLangString):
    
    print(inputLangString)
    translatedStr = translator.translate(inputLangString , dest='es')
    return translatedStr.text


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port='8080')