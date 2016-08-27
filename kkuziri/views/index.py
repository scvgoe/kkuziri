from flask import render_template
from kkuziri import app
from kkuziri.models import Category

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html', categories=Category.get_categories())
