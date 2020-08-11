## intiliasation file of our package
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask import flash, redirect, render_template, request, session, abort , url_for
from datetime import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = 'e62d0f1e6c4be7d0dbb47be2ebf8d004' # any random string
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#creating database
db = SQLAlchemy(app)

## due to circular imports we import at last
from web_app import routes