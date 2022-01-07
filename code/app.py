from flask import Flask
# Importar los controladores
from controllers.autor_rest_controller import autor_controller
from config import config

app = Flask(__name__)
# Controllers
# app.register_blueprint(item_api)
app.register_blueprint(autor_controller, url_prefix='/autor')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
