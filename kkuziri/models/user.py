from kkuziri import db, bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)
    _password = db.Column(db.String(128))
#    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def get_password(self):
        return self._password

#    @password.setter
    def set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._password, plaintext)
