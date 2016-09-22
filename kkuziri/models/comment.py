from kkuziri import db, bcrypt
from datetime import datetime

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
    def new_comment(body, author_id, post_id):
        comment = Comment(body, author_id, post_id)

        db.session.add(comment)
        db.session.commit()

        return comment

