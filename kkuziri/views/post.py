from flask import render_template, url_for
from kkuziri.models import User
from kkuziri import app

@app.route('/posts/<category>')
def posts():
    # show list of posts
    return render_template('posts.html')

@app.route('/post/<id>')
def post():
    # show post
    return render_template('post.html')

@app.route('/posts/<category>/new', methods=['GET, POST'])
def new_post():
    # new post
    return render_template('post_edit.html')

@app.route('/category/new', methods=['GET, POST'])
def new_category():
    # new category
    return

