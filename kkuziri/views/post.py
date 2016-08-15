from flask import render_template, url_for
from kkuziri.models import User
from kkuziri import app

@app.route('/posts/<category>', methods=['GET'])
def posts():
    # show list of posts
    return render_template('posts.html')

@app.route('/post/<post_id>', methods=['GET'])
def post():
    # show post
    return render_template('post.html')

#@app.route('/post/<category>/new', methods=['GET'])
@app.route('/post_new', methods=['GET'])
def post_new():
    # new post
    return render_template('post_edit.html')
