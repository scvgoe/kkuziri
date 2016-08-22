from kkuziri import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), index=True)
    posts = db.relationship('Post', backref='category', lazy='dynamic')

    parent_category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    sub_categories = db.relationship('Category', backref='parent_category', remote_side=[id])

    def __init__(self, name, parent_category_id=None):
        self.name = name
        if parent_category_id is not None:
            self.parent_category_id = parent_category_id

    def get_id(self):
        return self.id
