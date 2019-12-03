from flask import render_template

from app import app
from scrape import breeds


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', breeds=breeds)