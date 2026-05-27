import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-techbol'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///techbol.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False