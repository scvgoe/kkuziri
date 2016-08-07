from kkuziri import db
from kkuziri.models import User, Post, Category

def test_post():
    db.session.commit()
    db.drop_all()
    db.create_all()

    u = User('test_post_user', 'test_post_user')

    db.session.add(u)
    db.session.commit()

    c = Category('test_post_category')

    db.session.add(c)
    db.session.commit()

    p = Post('post_title', 'post_body', u.id, c)

    db.session.add(p)
    db.session.commit()

    posts = Post.query.order_by(Post.id)
    for post in posts:
        print 'title: %s, body: %s' % (post.title, post.body)
