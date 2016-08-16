from kkuziri import db
from kkuziri.models import User

def test_user():
    db.drop_all()
    db.create_all()

    for i in range(10):
        u = User('test_user_name_%d' % i, 'test_user_pw_%d' % i)
        db.session.add(u)

    users = User.query.order_by(User.username)

    print '--------------------- test result -------------------'
    for user in users:
        print 'user_name = %s' % user.username

    print 'test_user success!!!'
