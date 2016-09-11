from flask import render_template
from kkuziri import app

@app.route('/about')
def about():
    return render_template('about.html')
