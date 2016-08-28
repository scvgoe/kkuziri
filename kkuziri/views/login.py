from flask import render_template, redirect, flash, url_for, request, session
from kkuziri.models import User
from kkuziri import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = 'Invalid try'
    if request.method == 'POST':
        user = User.\
                    query.\
                    filter_by(username=request.form['username']).\
                    first()
        if (user is not None and
                user.is_correct_password(request.form['password'])):
            session['logged_in'] = True
            session['user_id'] = user.get_id()
            return redirect(url_for('index'))
        else:
            error = 'Invalid login'
            
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    return redirect(url_for('index'))
