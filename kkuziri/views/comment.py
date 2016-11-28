from flask import render_template, url_for, request, session, flash, redirect, abort
from kkuziri import app
from kkuziri.utils import Auth
from kkuziri.models import Comment

@app.route('/comments/<post_id>', methods=['POST'])
@Auth.auth_login
def new_comment(post_id):
    if request.method == 'POST':
        comment = Comment.new_comment(request.form.get('body'), session['user_id'], post_id)

        if comment != None:
            return redirect(url_for('get_post', id=post_id))

        else:
            return abort(404)
    
    else:
        return abort(405)
