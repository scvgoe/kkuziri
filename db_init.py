from kkuziri import app, db
from kkuziri.models import *

db.drop_all()
db.create_all()

admin = User("admin_id")
db.session.add(admin)
db.session.commit()

category = Category("default")
db.session.add(category)
db.session.commit()

post = Post("Hello, world!", "Hello, world!", admin.id, category.id)
db.session.add(post)
db.session.commit()

comment = Comment("Bye, world!", admin.id, post.id)
db.session.add(comment)
db.session.commit()
