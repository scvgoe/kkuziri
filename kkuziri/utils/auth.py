from flask import session
from kkuziri.models import Post, User
import kkuziri

class Auth():
    @staticmethod
    def auth_writer(original_function):
        def wrapper(*args, **kwargs):
            if is_writer(args[0]):
                return original_function(*args, **kwargs)

            #TODO return error page

        return wrapper

    @staticmethod
    def auth_master(original_function):
        def wrapper(*args, **kwargs):
            if is_master():
                return original_function(*args, **kwargs)

            #TODO return error page

        return wrapper

    @staticmethod
    def auth_login(original_function):
        def wrapper(*args, **kwargs):
            if is_login():
                return original_function(*args, **kwargs)

            #TODO return error page

        return wrapper

    @staticmethod
    def is_writer(post_id):
        post = Post.get_post(post_id)
        if post != None and 'user_id' in session:
            if post.author_id == session['user_id']:
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
