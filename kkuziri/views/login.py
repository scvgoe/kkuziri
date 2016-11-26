from flask import render_template, redirect, flash, url_for, request, session
from kkuziri.models import User, Post
from kkuziri import app, db
import json

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    elif request.method == 'POST':
        user = User.get_user(username=request.form['username'])
        if (user != None and
                user.is_correct_password(request.form['password'])):
            session['logged_in'] = True
            session['user_id'] = user.get_id()
            return redirect(url_for('index'))
        else:
            error = 'Invalid login'
            
    return render_template('login.html', error=error)

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
            session['logged_in'] = True
            session['user_id'] = user.get_id()
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    return redirect(url_for('login'))
