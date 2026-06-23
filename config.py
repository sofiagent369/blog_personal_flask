import os

class Config:
    # Variables de configuración generales
    DEBUG = True
    TESTING = False
    SECRET_KEY = 'your_secret_key_here'
    
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False