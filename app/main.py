from flask import Flask
from app.routes import bp
from app.config import config
import os

def create_app():
    app = Flask(__name__)
    env = os.environ.get('APP_ENV', 'default')
    app.config.from_object(config[env])
    app.register_blueprint(bp)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
