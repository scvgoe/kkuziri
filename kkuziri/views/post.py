from flask import render_template, url_for
from kkuziri.models import User
from kkuziri import app

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    # show list of posts
    return render_template('posts.html')

'''
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return render_template('index.html')
'''
