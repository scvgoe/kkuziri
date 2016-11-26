from kkuziri import db, bcrypt
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(128))
    _password = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    created_at = db.Column(db.DateTime)
    
    def __init__(self, username):
        self.username = username
        self.created_at = datetime.now()


    def get_comments(self):
        return self.comments

    def get_created_at(self):
        return self.created_at

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_posts(self):
        return self.posts

    @staticmethod
    def get_user(id=0, username=''):
        if id != 0:
            return User.query.get(id)

        elif username != '':
            return User.\
                query.\
                filter_by(username=username).\
                first()

        return None

    def get_username(self):
        return self.username

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)
    
    def set_name(self, name):
        self.name = name

    def set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)
