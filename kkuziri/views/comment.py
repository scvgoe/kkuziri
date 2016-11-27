from flask import render_template, url_for, request, session, flash, redirect
from kkuziri import app
from kkuziri.utils import Auth
from kkuziri.models import Comment

@app.route('/comments/<post_id>', methods=['POST'])
@Auth.auth_login
def new_comment(post_id):
    Comment.new_comment(request.form.get('body'), session['user_id'], post_id)

    return redirect(url_for('get_post', id=post_id))
