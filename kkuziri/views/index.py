from flask import render_template
from kkuziri import app
from kkuziri.models import Category, Post

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', page=Post.get_posts(per_page=5))

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html', categories=Category.get_categories())
