import os

class Config:
    '''
    General configuration parent class
    '''
   
    #API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://AbbyShabi:dammy@localhost/iblog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://AbbyShabi:dammy@localhost/iblog'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,

}