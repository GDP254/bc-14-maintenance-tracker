# config.py

# Enable Flask's debugging features. Should be False in production
DEBUG = True
SECRET_KEY = 'hard to guess string'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:simple101@localhost:5433/maintenance'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

MAIL_SERVER='smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'stvnkrs1@gmail.com'
MAIL_PASSWORD = 'ta1fac00l'
MAIL_USE_TLS = False
MAIL_USE_SSL = True

AT_USERNAME = 'stvnkrs'
AT_APIKEY = 'ecd8b59d5a637d8b473b8f121744acbc993300ab5543ac0a1a044de1191d728a'
PHONE_NUMBER = '+15005550006' #'+17606844938'



