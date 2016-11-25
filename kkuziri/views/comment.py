from flask import render_template, url_for, request, session, flash, redirect
from kkuziri import app
from kkuziri.models import Comment

@app.route('/comments/<post_id>', methods=['POST'])
def new_comment(post_id):
    if not 'logged_in' in session or session['logged_in'] is not True:
        flash('You have to be logged in')
        return render_template('index.html')

    Comment.new_comment(request.form.get('body'), session['user_id'], post_id)

    return redirect(url_for('posts', id=post_id))
