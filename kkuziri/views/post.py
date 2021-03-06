from flask import render_template, url_for, request, session, redirect, abort
from kkuziri import app, auth
from kkuziri.models import Category, Post, User

@app.route('/posts', methods=['POST'])
@auth.auth_master
def new_post():
    if request.method == 'POST':
        category_name = request.form.get('category').split('/')[-1]
        category = Category.get_category(category_name)
        user = User.get_user(id=session['user_id'])
        post = None

        if category != None and user != None:
            post = Post.new_post(request.form.get('title'),
                request.form.get('body'),
                session['user_id'],
                category.id,
                True if request.form.get('is_private') else False)

        if post != None:
            return redirect(url_for('get_post', id=post.id))

        else:
            return abort(404)

    else:
        return abort(405)

@app.route('/posts/<id>')
def get_post(id):
    if request.method == 'GET':
        post = Post.get_post(id)
        if post != None:
            return render_template('post.html', post=Post.get_post(id))
        
        else:
            return abort(404)

    else:
        return abort(405)

@app.route('/posts/<id>', methods=['POST'])
@auth.auth_post_writer
def edit_post(id):
    if request.method == 'POST':
        category_name = request.form.get('category').split('/')[-1]
        category = Category.get_category(category_name)
        user = User.get_user(id=session['user_id'])
        post = Post.get_post(id)

        if post != None and category != None and user != None:
            post = post.edit(request.form.get('title'),
                       request.form.get('body'),
                       category.id,
                       True if request.form.get('is_private') else False)
        
            return redirect(url_for('get_post', id=post.id))
        
        else:
            return abort(404)
    else:
        return abort(405)

@app.route('/posts/<id>/delete')
@auth.auth_post_writer_or_master
def delete_post(id):
    if request.method == 'GET':
        post = Post.get_post(id)
        if post != None:
            post.delete()
            return redirect(url_for('get_post_list'))
        
        else:
            return abort(404)

    else:
        return abort(405)

@app.route('/posts/edit')
@auth.auth_master
def get_post_creator():
    if request.method == 'GET':
        return render_template('post_new.html',
                categories=Category.get_categories())

    else:
        return(405)

@app.route('/posts/edit/<int:id>')
@auth.auth_post_writer
def get_post_editor(id):
    if request.method == 'GET':
        post = Post.get_post(id)
        if post != None:
            return render_template('post_edit.html', post=Post.get_post(id),
                    categories=Category.get_categories())

        else:
            return abort(404)
    
    else:
        return abort(405)

@app.route('/posts/list', defaults={'page': 1})
@app.route('/posts/list/<int:page>')
def get_post_list(page):
    if request.method == 'GET':
        return render_template('post_list.html', pagination=Post.get_posts(page=page))

    else:
        return abort(405)
