from flask import Flask

# Importar los controladores
from controllers.ItemRestController import item_api

app = Flask(__name__)

# Controllers
# app.register_blueprint(item_api)
app.register_blueprint(item_api, url_prefix='/item')


if __name__ == '__main__':
    app.run(debug=True)
