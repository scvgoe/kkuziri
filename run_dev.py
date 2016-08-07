from kkuziri import app, db
from tests import test_user, test_post

test_user()
test_post()

if __name__ == '__main__':
    app.run()
