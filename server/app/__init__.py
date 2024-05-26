from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://brcls:286723@localhost/electoralsystem'

    # Importa db aqui para evitar importação circular
    from .models import db

    db.init_app(app)
    migrate.init_app(app, db)

    # Importa o Blueprint de rotas aqui para evitar importação circular
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
