import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from src.infrastructure.database import db
from src.infrastructure.models import *
from src.api.v1.store import store_bp
from src.api.v1.category import category_bp
from src.api.v1.product import product_bp
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

CORS(app)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(store_bp)
app.register_blueprint(category_bp)
app.register_blueprint(product_bp)

if __name__ == "__main__":
    app.run(debug=True)