from flask import Flask, request
from flask_restplus import Resource, Api
from flask import jsonify


app = Flask(__name__)
api = Api(app)
# app.config["DEBUG"] = True

@api.route('/celsius/<int:temperatura>/fahrenheit')
class ConversaoCelsius(Resource):
    def get(self, temperatura):
        fahrenheit = (temperatura * 9 / 5) + 32
        return jsonify({ 'fahrenheit': fahrenheit })

@api.route('/fahrenheit/<int:temperatura>/celsius')
class ConversaoFahrenheit(Resource):
    def get(self, temperatura):
        celsius = (temperatura - 32) * 5 / 9
        return jsonify({ 'celsius': celsius })     

@app.route('/', methods=['GET'])
def home():
    return "Api de Conversão em Python"

if __name__ == '__main__':
    app.run()
