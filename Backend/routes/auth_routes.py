from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from extensions import db
import jwt, datetime
from flask import current_app as app

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data["password"])
    user = User(username=data["username"], email=data["email"], password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg" : "User registered successfully"})

@auth_bp.routes("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = user.query.filter_by(email=data["email"]).first()
    if user and check_password_hash(user.password, data["password"]):
        token = jwt.encode({"id" : user.id, "exp" : datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, app.config["SECRET_KEY"], algorithm="HS256")
        return jsonify({"token" : token})
    return jsonify({"msg" : "Invalid credentials"}), 401