from flask import session, abort
from functools import wraps
from kkuziri.models import Post, Comment
import kkuziri

class Auth():
    def auth_post_writer(self, original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if self.is_post_writer(kwargs['id']):
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    def auth_comment_writer(self, original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if self.is_comment_writer(kwargs['id']):
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    def auth_post_writer_or_master(self, original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if self.is_post_writer(kwargs['id']) or self.is_master():
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    def auth_comment_writer_or_master(self, original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if self.is_comment_writer(kwargs['id']) or self.is_master():
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    def auth_master(self, original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if self.is_master():
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    def auth_login(self, original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if self.is_login():
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    def is_post_writer(self, post_id):
        post = Post.get_post(post_id)
        if post != None and 'user_id' in session:
            if post.author_id == session['user_id']:
                return True

        return False

    def is_comment_writer(self, comment_id):
        comment = Comment.get_comment(comment_id)
        if comment != None and 'user_id' in session:
            if comment.author_id == session['user_id']:
                return True

        return False

    def is_master(self):
        if 'user_id' in session and session['user_id'] != None:
            if session['user_id'] in kkuziri.MASTER:
                return True

        return False

    def is_login(self):
        if 'user_id' in session and session['user_id'] != None:
            return True

        return False
