from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def db():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    return SQLAlchemy(app)
