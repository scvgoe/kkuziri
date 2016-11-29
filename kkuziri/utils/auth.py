from flask import session, abort
from functools import wraps
from kkuziri.models import Post, Comment
import kkuziri

class Auth():
    @staticmethod
    def auth_post_writer(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if Auth.is_post_writer(kwargs['id']):
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    @staticmethod
    def auth_comment_writer(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if Auth.is_comment_writer(kwargs['id']):
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    @staticmethod
    def auth_post_writer_or_master(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if Auth.is_post_writer(kwargs['id']) or Auth.is_master():
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    @staticmethod
    def auth_comment_writer_or_master(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if Auth.is_comment_writer(kwargs['id']) or Auth.is_master():
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    @staticmethod
    def auth_master(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if Auth.is_master():
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    @staticmethod
    def auth_login(original_function):
        @wraps(original_function)
        def wrapper(*args, **kwargs):
            if Auth.is_login():
                return original_function(*args, **kwargs)

            return abort(403)

        return wrapper

    @staticmethod
    def is_post_writer(post_id):
        post = Post.get_post(post_id)
        if post != None and 'user_id' in session:
            if post.get_author_id() == session['user_id']:
                return True

        return False

    @staticmethod
    def is_comment_writer(comment_id):
        comment = Comment.get_comment(comment_id)
        if comment != None and 'user_id' in session:
            if comment.get_author_id() == session['user_id']:
                return True

        return False

    @staticmethod
    def is_master():
        if 'user_id' in session and session['user_id'] != None:
            if session['user_id'] in kkuziri.MASTER:
                return True

        return False

    @staticmethod
    def is_login():
        if 'user_id' in session and session['user_id'] != None:
            return True

        return False
