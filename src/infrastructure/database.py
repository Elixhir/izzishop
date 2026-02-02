from flask_sqlalchemy import SQLAlchemy

class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = SQLAlchemy()
        return cls._instance

db = Database()