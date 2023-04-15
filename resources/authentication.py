import functools
from flask_restful import Resource, abort
from flask import request, current_app as app
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

from controllers.authController import AuthController
from config import config

authController = AuthController()

def login_required(method):
    @functools.wraps(method)
    def wrapper(self):
        header = request.headers.get('Authorization')
        _, token = header.split()
        try:
            decoded = jwt.decode(token, config['JWT_KEY'], algorithms='HS256')
        except jwt.DecodeError:
            abort(400, message='Token is not valid')
        except jwt.ExpiredSignatureError:
            abort(400, message='Token is expired')
        user_email = decoded['email']
        res = authController.find({ "email": user_email })
        if len(res) == 0:
            abort(400, message='Token is not from a valid user')
        user = res[0]
        user.pop('password')
        return method(self, user)
    return wrapper

class Register(Resource):
    def post(self):
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        phone = request.json['phone']
        app.logger.info(f"New User Data Log: {name, email, phone}")
        if email is None or password is None:
            abort(403, message="Invalid Input")
        if len(authController.find({ "email": email })) != 0:
            abort(403, message="User Already Exists")
        res = authController.create({ "name": name, "email": email, "phone": phone, "password": generate_password_hash(password) })
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=config['TOKEN_EXPIRE_HOURS'])
        encoded = jwt.encode({'email': email, "exp": exp}, config['JWT_KEY'], algorithm='HS256')
        return { "data": res, "token": encoded }, 200

class Login(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']
        app.logger.info(f"User Login Log: {email}")
        if email is None or password is None:
            abort(403, message="Invalid Input")
        res = authController.find({ "email": email })
        if len(res) == 0:
            abort(403, message="User Not Found")
        user = res[0]
        if not check_password_hash(user['password'], password):
            abort(400, message='Password is incorrect')
        user.pop('password')
        exp = datetime.datetime.utcnow() + datetime.timedelta(hours=config['TOKEN_EXPIRE_HOURS'])
        encoded = jwt.encode({'email': email, 'exp': exp}, config['JWT_KEY'], algorithm='HS256')
        return { "data": user, "token": encoded }, 200