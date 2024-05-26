from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from flask_cors import CORS

metadata = MetaData(naming_convention={
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})

app = Flask(__name__)
cors = CORS(app, support_credentials=True, origins='*')
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(metadata=metadata)
migrate = Migrate()

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://brcls:286723@localhost/electoralsystem'

    from .models import db

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
