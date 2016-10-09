from kkuziri import db, bcrypt
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    _password = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    created_at = db.Column(db.DateTime)
    
    def __init__(self, username, plaintext):
        self.username = username
        self.set_password(plaintext)
        self.created_at = datetime.now()

    def get_id(self):
        return self.id

    def get_password(self):
        return self._password

    @staticmethod
    def get_user(id):
        return User.query.get(id)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)
    
    def set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)
