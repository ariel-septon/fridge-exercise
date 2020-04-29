from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import app_config
from flask_migrate import Migrate

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

print(app_config.items())


def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(app_config[config_name])
    # app_config[config_name].init_app(app)
    import os
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://refrigerator_ex:my_db@localhost/refrigerator_db'
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    migrate = Migrate(app, db)
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .classes.item import item as item_blueprint
    app.register_blueprint(item_blueprint)
    from .classes.shelf import shelf as shelf_blueprint
    app.register_blueprint(shelf_blueprint)
    from .classes.refrigerator import refrigerator as refrigerator_blueprint
    app.register_blueprint(refrigerator_blueprint)
    from app import models

    return app
