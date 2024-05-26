from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://brcls:286723@localhost/electoralsystem'
    db.init_app(app)
    migrate.init_app(app, db)

    from . import routes, models  # Importando rotas e modelos

    return app
