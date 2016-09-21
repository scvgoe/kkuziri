from flask import render_template, url_for, request, session, flash, redirect
from kkuziri.models import User, Category, Post
from kkuziri import app

@app.route('/posts', defaults={'page': 1})
@app.route('/posts/<page>')
def posts(page):
    return render_template('posts.html',
                            pagination=Post.get_posts(page=int(page)))

@app.route('/posts/<category>/<page>')
def posts_from_category(category, page):
    # show list of posts
    # including all subcategory's posts
    return render_template('posts.html',
            pagination=Post.get_posts(category_name=category,
                                      page=int(page)))

@app.route('/post/<id>')
def post(id):
    return render_template('post.html', post=Post.get_post(id))

@app.route('/post/edit/<id>', methods=['GET', 'POST'])
def edit_post(id):
    # edit post

    # TODO
    # form validation check

    if not 'logged_in' in session or session['logged_in'] is not True:
        flash('You have to be logged in')
        return render_template('index.html')

    if request.method == 'GET':
        return render_template('post_edit.html', post=Post.get_post(id),
                            categories=Category.get_categories())

    elif request.method == 'POST':
        post=Post.get_post(id)
        post.edit_post(request.form.get('title'),
                       request.form.get('body'),
                       request.form.get('category').split('/')[-1])
        
        return redirect(url_for('post', id=post.id))

@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    # new post

    # TODO
    # form validation check

    if not 'logged_in' in session or session['logged_in'] is not True:
        flash('You have to be logged in')
        return render_template('index.html')

    if request.method == 'GET':
        return render_template('post_new.html',
                categories=Category.get_categories())

    elif request.method == 'POST':
        post = Post.new_post(request.form.get('title'),
                             request.form.get('body'),
                             session['user_id'],
                             request.form.get('category').split('/')[-1])

        return redirect(url_for('post', id=post.id))

@app.route('/post/<id>/delete')
def delete_post():
    # delete post
    # category = post<id>'s category
    return redirect(url_for('posts', category=category))
