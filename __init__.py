from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://virajs:visadev@localhost:5432/my_test'

db.init_app(app)
