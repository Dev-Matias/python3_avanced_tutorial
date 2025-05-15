from flask import Flask, jsonify

app = Flask(__name__)

libro = {
    "titulo": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967,
    "genero": "Realismo mágico"
}

@app.route('/libro', methods=['GET'])
def obtener_libro():
    return jsonify(libro)

if __name__ == '__main__':
    app.run(debug=True)