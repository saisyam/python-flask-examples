from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    title = "Flask templates with params"
    return render_template('index.html', title=title)