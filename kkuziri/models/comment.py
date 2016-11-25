from datetime import datetime
from kkuziri import db, bcrypt
from post import *

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.String(64))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, body, author_id, post_id):
        self.body = body
        self.author_id = author_id
        self.post_id = post_id
        self.created_at = datetime.now()

    @staticmethod
    def is_valid(body, author_id, post_id):
        if body == None or body == '':
            return False

        if Post.get_post(id) == None:
            return False

        return True

    @staticmethod
    def new_comment(body, author_id, post_id):
        if not is_valid(body, author_id, post_id):
            return None

        comment = Comment(body, author_id, post_id)

        db.session.add(comment)
        db.session.commit()

        return comment
