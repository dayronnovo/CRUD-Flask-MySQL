class DevelopmentConfig:
    DEBUG = True
    SERVER_NAME = '127.0.0.1:5010'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
