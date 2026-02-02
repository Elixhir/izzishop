import os
from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from src.infrastructure.database import db
from src.infrastructure.models import *

load_dotenv()

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)