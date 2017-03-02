from datetime import datetime
from kkuziri import db, bcrypt

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    deleted_at = db.Column(db.DateTime)

    def __init__(self, body, author_id, post_id):
        self.body = body
        self.author_id = author_id
        self.post_id = post_id
        self.created_at = datetime.now()

    def delete(self):
        self.deleted_at = datetime.now()

        db.session.commit()

    @staticmethod
    def get_comment(id):
        comment = Comment.query.get(id)

        if comment.deleted_at == None:
            return comment

        return None

    @staticmethod
    def is_valid(body, author_id):
        if body == None or body == '':
            return False

        return True

    @staticmethod
    def new_comment(body, author_id, post_id):
        if not Comment.is_valid(body, author_id):
            return None

        comment = Comment(body, author_id, post_id)

        db.session.add(comment)
        db.session.commit()

        return comment
