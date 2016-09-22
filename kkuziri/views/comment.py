from flask import render_template, url_for, request, session, flash, redirect
from kkuziri.models import Comment
from kkuziri import app

@app.route('/comment/new/<post_id>', methods=['POST'])
def new_comment(post_id):
    # new comment

    # TODO
    # form validation check

    if not 'logged_in' in session or session['logged_in'] is not True:
        flash('You have to be logged in')
        return render_template('index.html')

    comment = Comment.new_comment(request.form.get('body'),
                                  session['user_id'],
                                  post_id)

    return redirect(url_for('post', id=post_id))
