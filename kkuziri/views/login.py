from flask import render_template, redirect, url_for, request, session, abort
from kkuziri import app, db
from kkuziri.models import User, Post
from kkuziri.utils import Auth
import json

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        user = User.get_user(username=request.form['username'])
        if (user != None and
                user.is_correct_password(request.form['password'])):
            session['user_id'] = user.get_id()
            return redirect(url_for('index'))

    else:
        return abort(405)

@app.route('/login/facebook', methods=['POST'])
def login_facebook():
    if request.method == 'POST':
        user = User.get_user(username=request.json['username'])
        if (user is None):
            user = User(request.json['username']) 
            user.set_name(request.json['name'])
            
            db.session.add(user)
            db.session.commit()

        if (user is not None):
            session['user_id'] = user.get_id()
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

    else:
        return abort(405)

@Auth.auth_login
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))
