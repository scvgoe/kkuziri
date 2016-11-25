from flask import render_template, url_for, request, session, flash, redirect
from kkuziri.models import User, Category, Post
from kkuziri import app

@app.route('/posts', methods=['POST'])
def new_post():
    post = Post.new_post(request.form.get('title'),
            request.form.get('body'),
            session['user_id'],
            request.form.get('category').split('/')[-1])

    if post != None:
        return redirect(url_for('get_post', id=post.id))

@app.route('/posts/<id>', methods=['GET'])
def get_post(id):
    if request.method == 'GET':
        post = Post.get_post(id)
        if post != None:
            return render_template('post.html', post=Post.get_post(id))

@app.route('/posts/<id>', methods=['POST'])
def edit_post(id):
    if request.method == 'POST':
        post = Post.get_post(id)

        if post != None:
            post = post.edit(request.form.get('title'),
                       request.form.get('body'),
                       request.form.get('category').split('/')[-1])
        
        return redirect(url_for('get_post', id=post.id))

@app.route('/posts/<id>', methods=['DELETE'])
def delete_post(id):
    if request.method == 'DELETE':
        post = Post.get_post(id)
        if post != None:
            post.delete()
            return redirect(url_for('get_post_list'))

@app.route('/posts/edit', defaults={'id': None})
@app.route('/posts/edit/<int:id>', methods=['GET'])
def get_post_editor(id):
    if id == None:
        return render_template('post_new.html',
                categories=Category.get_categories())
    else:
        if request.method == 'GET':
            post = Post.get_post(id)
            if post != None:
                return render_template('post_edit.html', post=Post.get_post(id),
                        categories=Category.get_categories())

@app.route('/posts/list', defaults={'page': 1})
@app.route('/posts/list/<int:page>')
def get_post_list(page):
    return render_template('post_list.html', pagination=Post.get_posts(page=page))
