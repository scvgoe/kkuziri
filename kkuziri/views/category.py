from flask import render_template, url_for, request, redirect, abort
from kkuziri import app, db
from kkuziri.models import Category
from kkuziri.utils import Auth

@app.route('/categories', methods=['GET', 'POST'])
@Auth.auth_master
def new_category():
    if request.method == 'GET':
        return redirect(url_for('test'))
        
    elif request.method == 'POST':
        parent_name = request.form.get('parent_name').split('/')[-1]
        name = request.form.get('name')
        parent = Category.get_category(parent_name)

        if (parent_name == 'Root'):
            category = Category(name)
        else:
            category = Category(name, parent.id)

        db.session.add(category)
        db.session.commit()
        return redirect(url_for('test'))

    else:
        return abort(405)
