# config.py

# Enable Flask's debugging features. Should be False in production
DEBUG = True
SECRET_KEY = 'hard to guess string'
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:simple101@localhost:5433/maintenance'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = False


