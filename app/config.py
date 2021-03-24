import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = 'postgres://pkpcxjetcvmvda:8e06e8f57beaee2d8114a3ab58873fce4e8d5f2ec8f31340b17e7159354539c3@ec2-54-235-108-217.compute-1.amazonaws.com:5432/d63ig4d4c5qpa8' or 'postgresql://project1:password123@localhost/project1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './uploads/'

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False