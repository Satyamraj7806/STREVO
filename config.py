# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'thisissecret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///strevo.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
