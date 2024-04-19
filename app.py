from flask import Flask  # Incial config.
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from flask_migrate import Migrate
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(contacts)


