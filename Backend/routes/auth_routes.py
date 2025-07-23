from flask import Blueprint, request, jsonify
from services.auth_service import register_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    user = register_user(data["username"], data["email"], data["password"])
    return jsonify({"msg" : "User registered", "user_id" : user.id})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    token = authenticate_user(data["email"], data["password"])
    if token:
        return jsonify({"token" : token})
    return jsonify({"msg" : "Invalid credentials"}), 401