from app import app  # to import app from app.py
from utils.db import db

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)  # to update the changes
