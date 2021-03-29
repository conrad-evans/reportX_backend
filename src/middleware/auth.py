from functools import wraps
from flask import request
import jwt


def loginRequired(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        token = request.headers.get('token')
        if token is None:
            return "no token provided"
        try:
            decoded_token = jwt.decode(token, "changethis")
        except Exception as e:
            print(e)
            return "invalid token"

        return view(*args, **kwargs, uid=decoded_token['uid'])

    return wrapped_view
