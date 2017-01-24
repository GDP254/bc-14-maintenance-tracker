from app import app
from flask.ext.bootstrap import Bootstrap

bootstrap = Bootstrap(app)
if __name__ == '__main__':
    app.run()