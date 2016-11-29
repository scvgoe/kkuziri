from flask import render_template, url_for, request, session, redirect, abort
from kkuziri import app
from kkuziri.models import Category, Post
from kkuziri.utils import Auth

@app.route('/posts', methods=['POST'])
@Auth.auth_master
def new_post():
    if request.method == 'POST':
        post = Post.new_post(request.form.get('title'),
                request.form.get('body'),
                session['user_id'],
                request.form.get('category').split('/')[-1])

        if post != None:
            return redirect(url_for('get_post', id=post.get_id()))

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
@Auth.auth_writer
def edit_post(id):
    if request.method == 'POST':
        post = Post.get_post(id)

        if post != None:
            post = post.edit(request.form.get('title'),
                       request.form.get('body'),
                       request.form.get('category').split('/')[-1])
        
            return redirect(url_for('get_post', id=post.get_id()))
        
        else:
            return abort(404)
    else:
        return abort(405)

@app.route('/posts/<id>/delete')
@Auth.auth_post_writer_or_master
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
@Auth.auth_master
def get_post_creator():
    if request.method == 'GET':
        return render_template('post_new.html',
                categories=Category.get_categories())

    else:
        return(405)

@app.route('/posts/edit/<int:id>')
@Auth.auth_post_writer
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
