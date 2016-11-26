from datetime import datetime
from kkuziri import db, bcrypt
from post import *

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.String(64), db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, body, author_id, post_id):
        self.body = body
        self.author_id = author_id
        self.post_id = post_id
        self.created_at = datetime.now()

    def get_author(self):
        return self.author

    def get_author_id(self):
        return self.author_id

    def get_body(self):
        return self.body

    def get_created_at(self):
        return self.created_at

    def get_id(self):
        return self.id

    def get_modified_at(self):
        return self.modified_at

    def get_post_id(self):
        return self.post_id

    @staticmethod
    def is_valid(body, author_id, post_id):
        if body == None or body == '':
            return False

        if Post.get_post(id) == None:
            return False

        return True

    @staticmethod
    def new_comment(body, author_id, post_id):
        if not Comment.is_valid(body, author_id, post_id):
            return None

        comment = Comment(body, author_id, post_id)

        db.session.add(comment)
        db.session.commit()

        return comment
