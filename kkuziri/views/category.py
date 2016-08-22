from flask import render_template, url_for, request
from kkuziri.models import Category
from kkuziri import app, db

@app.route('/category/new', methods=['GET, POST'])
def new_category():
    if request.method == 'POST':
        name = request.form.get('name')
        parent_category_id = request.form.get('parent_category_id')
        
        category = Category(name, parent_category_id=parent_category_id)
        db.add(category)

    return redirect(url_for('posts', category=category.get_id()))
