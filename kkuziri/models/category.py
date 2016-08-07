from kkuziri import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    parent_category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    sub_categories = db.relationship('Category', backref='parent_category', remote_side=[id])

    def __init__(self, name):
        self.name = name
