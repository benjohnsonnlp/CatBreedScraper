from flask import render_template

from app import app
from app.model import Kitty


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', kitties=Kitty.query.all())