import os

class Config:
    '''
    General configuration parent class
    '''
<<<<<<< HEAD
   
    API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://AbbyShabi:dammy@localhost/iblog'
=======
    FLIGHT_API_BASE_URL ='https://dev-sandbox-api.airhob.com/sandboxapi/activities/v1/search{}?api_key={}''
    FLIGHT_API_KEY = os.environ.get('FLIGHT_API_KEY')
>>>>>>> aaf072ed9e45d0feb4f0bf9cb79421631549f977
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
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
   
    pass



class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,

}