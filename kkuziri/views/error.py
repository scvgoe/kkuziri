# -*- coding: utf-8 -*-

from flask import render_template
from kkuziri import app

@app.errorhandler(403)
def error_403(e):
    return render_template('error.html', error="You do not have permission to access."), 401

@app.errorhandler(404)
def error_404(e):
    return render_template('error.html', error="The page you requested could not be found."), 404

@app.errorhandler(405)
def error_405(e):
    return render_template('error.html', error="Invalid request."), 405

@app.errorhandler(500)
def error_500(e):
    return render_template('error.html', error="An error has occurred on the server."), 500
