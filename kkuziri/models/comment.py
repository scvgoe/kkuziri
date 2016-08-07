from kkuziri import db, bcrypt
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.Text)
    author_name = db.Column(db.String(64))
    _password = db.Column(db.String(128))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, body, author_name, password, post_id):
        self.body = body
        self.author_name = author_name
        self.post_id = post_id
        slef.create_at = datetime.now()
        self.set_password(password)

    def get_password(self):
        return self._password

    def set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)

