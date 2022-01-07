class DevelopmentConfig:
    DEBUG = True
    # SERVER_NAME = '127.0.0.1:5010' #Pincha perfecto
# Es para usar MySQL con el SQLArquemy
    # MYSQL_HOST = 'localhost'
    # MYSQL_USER = 'root'
    # MYSQL_PASSWORD = '5303@Root$'
    # MYSQL_DB = 'curso_flask_2'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
