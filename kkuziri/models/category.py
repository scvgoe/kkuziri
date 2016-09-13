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

    def get_full_name(self):
        full_name = self.name
        
        parent_id = self.parent_category_id
        while (parent_id is not None):
            parent = Category.query.get(parent_id)
            full_name = parent.name + '/' + full_name
            parent_id = parent.parent_category_id
        db.session.commit()

        return full_name

    @staticmethod
    def get_category(name):
        category = Category.query.filter_by(name=name).first()
        db.session.commit()
        return category

    @staticmethod
    def get_categories():
        categories = Category.query.order_by(Category.name)
        db.session.commit()
        return categories

    def get_posts(self):
        return self.posts
