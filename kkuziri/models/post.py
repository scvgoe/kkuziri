from kkuziri import db
from datetime import datetime

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

    def __init__(self, title, body, author_id, category_id):
        self.title = title
        self.body = body
        self.author_id = author_id
        self.created_at = datetime.now()
        self.views = 0
        self.category_id = category_id

    def delete(self):
        self.deleted_at = datetime.now()

        db.session.commit()

    def edit(self, title, body, category_id):
        if not Post.is_valid(title, body):
            return self 

        self.title = title
        self.body = body
        self.category_id = category_id
        self.modified_at = datetime.now()

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
            return post

        return None

    @staticmethod
    def get_posts(page=1, per_page=10):
        posts = Post.query.\
                filter_by(deleted_at=None).\
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
    def new_post(title, body, author_id, category_id):
        if not Post.is_valid(title, body):
            return None

        post = Post(title, body, author_id, category_id)
        db.session.add(post)
        db.session.commit()

        return post
