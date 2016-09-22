from kkuziri import db
from datetime import datetime
from category import * 
from comment import *

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(120), index=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    views = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __init__(self, title, body, author_id, category_id):
        self.title = title
        self.body = body
        self.author_id = author_id
        self.created_at = datetime.now()
        self.views = 0
        self.category_id = category_id

    @staticmethod
    def get_post(id):
        return Post.query.get(id)

    @staticmethod
    def get_posts(category_name=None, page=1, per_page=10):
        if (category_name==None):
            posts = Post.query.\
                    order_by(Post.created_at.desc()).\
                    paginate(page, per_page=per_page)
        else:
            # TODO category name validation check
            category = Category.get_category(category_name)
            posts = category.get_posts(page=page, per_page=per_page)

        return posts

    @staticmethod
    def new_post(title, body, author_id, category_name):
        category = Category.get_category(category_name)
        post = Post(title, body, author_id, category.id)
        db.session.add(post)
        db.session.commit()

        return post

    def edit_post(self, title, body, category_name):
        self.title = title
        self.body = body
        self.category = Category.get_category(category_name)
        self.modified_at = datetime.now()

        db.session.commit()

    def get_comments(self):
        return self.comments.order_by(Comment.created_at.desc())
