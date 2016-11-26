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

    @staticmethod
    def get_categories():
        categories = Category.query.order_by(Category.name)
        return categories

    @staticmethod
    def get_category(name):
        category = Category.query.filter_by(name=name).first()
        return category

    def get_full_name(self):
        full_name = self.name
        
        parent_id = self.parent_category_id
        while (parent_id is not None):
            parent = Category.query.get(parent_id)
            full_name = parent.name + '/' + full_name
            parent_id = parent.parent_category_id

        return full_name

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_parent_category(self):
        return self.parent_category

    def get_parent_category_id(self):
        return self.parent_category_id

    def get_posts(self, page=1, per_page=10):
        return self.posts.order_by(Post.created_at.desc()).\
                    paginate(page, per_page=per_page)
    def get_sub_categories(self):
        return self.sub_categories
