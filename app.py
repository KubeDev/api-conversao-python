import flask
import logging
import os 

app = flask.Flask(__name__)

logFile = os.getenv('LOG_FILE', default='application.log')

logging.basicConfig(format='%(asctime)s %(message)s',filename=logFile, level=logging.INFO)

@app.route('/', methods=['GET'])
def home():
    return "Api de Conversão em Python-v2"


@app.route('/celsius/<int:temperatura>/fahrenheit', methods=['GET'])
def celsius_fahrenheit(temperatura=None):
    fahrenheit = (temperatura * 9 / 5) + 32
    logging.info('Retornando o valor de conversao celsius %s para fahrenheit %s', temperatura, fahrenheit)
    return flask.jsonify({'fahrenheit': fahrenheit})


@app.route('/fahrenheit/<int:temperatura>/celsius', methods=['GET'])
def fahrenheit_celsius(temperatura=None):
    celsius = (temperatura - 32) * 5 / 9
    logging.info('Retornando o valor de conversao fahrenheit %s para celsius %s', temperatura, celsius)
    return flask.jsonify({'celsius': celsius})


if __name__ == '__main__':
    logging.debug('Servidor de debug iniciado')
    app.run(debug=True)
