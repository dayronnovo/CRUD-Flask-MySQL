from flask import Flask
# Importar configuracion
from config import config
# Importar los controladores
from controllers.item_rest_controller import item_api

app = Flask(__name__)

# Controllers
# app.register_blueprint(item_api)
app.register_blueprint(item_api, url_prefix='/item')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
