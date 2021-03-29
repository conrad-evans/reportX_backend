from functools import wraps
from datetime import datetime, timedelta
from flask import Blueprint, request
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from src.db import DataBase
from src.middleware import auth


auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

db = DataBase()


@auth_blueprint.route('/login', methods=['POST'])
def login():
    email = request.get_json()["email"]
    password = request.get_json()["password"]

    user = db.userInDB(email)
    if user is None:
        return "Invalid credentials"

    isMatch = check_password_hash(user['password'], password)
    if not isMatch:
        return "Invalid credentials"

    try:
        jwt_payload = {
            "uid": user['id'],
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(jwt_payload, key="changethis")
        return token
    except Exception as e:
        return "server error"


@auth_blueprint.route('/register', methods=['POST'])
def register():
    email = request.get_json()["email"]
    password = request.get_json()["password"]

    user = db.userInDB(email)
    if user:
        return "User already exists"

    hashed_password = generate_password_hash(password, salt_length=10)

    user_data = {
        'email': email,
        'password': hashed_password
    }
    user = db.saveUser(user_data)
    if not user:
        return "server error"

    try:
        jwt_payload = {
            "uid": user['id'],
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=1)
        }
        token = jwt.encode(jwt_payload, key="changethis")
        return token
    except Exception as e:
        return "server error"


@auth_blueprint.route('/logout', methods=['POST'])
@auth.loginRequired
def logout():
    return "logged out"
