from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)
    cors = CORS(app, resources={
        r"/*": {
            "origins": "*"
        }
    })
    db.init_app(app)
    from app.main.routes import main
    app.register_blueprint(main)

    return app

