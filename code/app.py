from flask import Flask
# Importar los controladores
from controllers.autor_rest_controller import autor_controller
from controllers.libro_rest_controller import libro_controller
from config import config

app = Flask(__name__)

# Controllers
app.register_blueprint(autor_controller, url_prefix='/autor')
app.register_blueprint(libro_controller, url_prefix='/libro')

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
