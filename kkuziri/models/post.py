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
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __init__(self, title, body, author_id, category_id):
        self.title = title
        self.body = body
        self.author_id = author_id
        self.created_at = datetime.now()
        self.views = 0
        self.category_id = category_id
