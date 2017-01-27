# config.py
import os

# Enable Flask's debugging features. Should be False in production
DEBUG = os.environ.get('DEBUG')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_COMMIT_ON_TEARDOWN = os.environ.get('SQLALCHEMY_COMMIT_ON_TEARDOWN')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

MAIL_SERVER=os.environ.get('MAIL_SERVER')
MAIL_PORT =os.environ.get('MAIL_PORT')
MAIL_USERNAME =os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD =os.environ.get('MAIL_PASSWORD')
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')

AT_USERNAME = os.environ.get('AT_USERNAME')
AT_APIKEY = os.environ.get('AT_APIKEY')



