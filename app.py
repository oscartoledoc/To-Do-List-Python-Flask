from flask import Flask  # Incial config.
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
from utils.db import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/contactsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(contacts)


