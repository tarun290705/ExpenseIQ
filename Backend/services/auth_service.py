from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from extensions import db
import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app

def register_user(username, email, password):
    hashed_pw = generate_password_hash(password)
    user = User(username=username, email=email, password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
        token = jwt.encode({
            "id" : user.id,
            "exp": datetime.now(timezone.utc) + timedelta(hours=24)
        }, current_app.config["SECRET_KEY"], algorithm="HS256")
        return token
    return None