# region
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, email

import os
# endregion

app = Flask(__name__)

bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')

@app.route('/')
def index():
    return render_template('index.html')