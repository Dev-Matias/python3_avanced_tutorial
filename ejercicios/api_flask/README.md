crea un entornovirtual para ejecutar el script
[]: # ```bash
[]: # python3 -m venv venv
[]: # source venv/bin/activate
[]: # ```
[]: # 
[]: # ## **4. Flask**  
[]: # ### **Instalación de Flask**  
[]: # ```bash
[]: # pip install Flask
[]: # ```
[]: # ### **Crear una aplicación Flask básica**  
[]: # ```python
[]: # from flask import Flask
[]: # app = Flask(__name__)
[]: # 
[]: # @app.route('/')
[]: # def hello():
[]: #     return "¡Hola, mundo!"
[]: # 
[]: # if __name__ == '__main__':
[]: #     app.run(debug=True)