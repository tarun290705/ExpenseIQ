from functools import wraps
from flask import request, jsonify
import jwt
from models.user import User
from extensions import db
from flask import current_app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split("")[-1]

        if not token:
            return jsonify({"msg" : "Token is missing!"}), 401
        
        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.filter_by(id=data["id"]).first()
        except:
            return jsonify({"msg" : "Token is invalid!"}), 401
        
        return f(current_user, *args, **kwargs)
    return decorated