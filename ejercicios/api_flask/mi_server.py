from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Hola, {nombre}!'

@app.route('/sumar/<int:a>/<int:b>')
def sumar(a, b):
    return str(a + b)

if __name__ == '__main__':
    app.run(debug=True)

