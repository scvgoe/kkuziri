from kkuziri import db
from datetime import datetime
from flask import session
from sqlalchemy import or_, and_

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), index=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    views = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    comments = db.relationship('Comment', order_by='desc(Comment.created_at)', backref='post', lazy='dynamic')
    deleted_at = db.Column(db.DateTime)
    is_private = db.Column(db.Boolean)

    def __init__(self, title, body, author_id, category_id, is_private):
        self.title = title
        self.body = body
        self.author_id = author_id
        self.created_at = datetime.now()
        self.views = 0
        self.category_id = category_id
        self.is_private = is_private

    def delete(self):
        self.deleted_at = datetime.now()

        db.session.commit()

    def edit(self, title, body, category_id, is_private):
        if not Post.is_valid(title, body):
            return self 

        self.title = title
        self.body = body
        self.category_id = category_id
        self.modified_at = datetime.now()
        self.is_private = is_private 

        db.session.commit()

        return self

    def get_author(self):
        return self.author

    def get_author_id(self):
        return self.author_id

    def get_body(self):
        return self.body

    def get_category(self):
        return self.category

    def get_category_id(self):
        return self.category_id

    def get_comments(self):
        return self.comments.filter_by(deleted_at=None)

    def get_created_at(self):
        return self.created_at

    def get_id(self):
        return self.id

    def get_is_private(self):
        return self.is_private

    def get_modified_at(self):
        return self.modified_at

    def get_title(self):
        return self.title

    def get_views(self):
        return self.views

    @staticmethod
    def get_post(id):
        post = Post.query.get(id)
        
        if post != None and post.deleted_at == None:
            if ((post.is_private != True) or
                    (post.is_private == True and
                        'user_id' in session and
                        post.author_id == session['user_id'])):
                return post

        return None

    @staticmethod
    def get_posts(page=1, per_page=10):
        if ('user_id' in session):
            posts = Post.query.\
                    filter_by(deleted_at=None).\
                    filter(or_(Post.is_private != True,
                               and_(Post.is_private ==  True,
                                    Post.author_id == session['user_id']))).\
                    order_by(Post.created_at.desc()).\
                    paginate(page, per_page=per_page)

        else:
            posts = Post.query.\
                    filter_by(deleted_at=None).\
                    filter(Post.is_private != True).\
                    order_by(Post.created_at.desc()).\
                    paginate(page, per_page=per_page)

        return posts

    @staticmethod
    def is_valid(title, body):
        if title == None or title == '':
            return False
        
        if body == None or body == '':
            return False
        
        return True

    @staticmethod
    def new_post(title, body, author_id, category_id, is_private):
        if not Post.is_valid(title, body):
            return None

        post = Post(title, body, author_id, category_id, is_private)
        db.session.add(post)
        db.session.commit()

        return post
