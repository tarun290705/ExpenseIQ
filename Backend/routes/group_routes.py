from flask import Blueprint, request, jsonify
from models.group import Group, GroupMember
from extensions import db
from utils.decorators import token_required

group_bp = Blueprint("groups", __name__)

@group_bp.route("/", methods=["POST"])
@token_required
def create_group(current_user_id):
    data = request.json
    group = Group(name=data["name"])
    db.session.add(group)
    db.session.commit()

    gm = GroupMember(user_id=current_user_id, group_id=group.id, role="admin")
    db.session.add(gm)
    db.session.commit()
    return jsonify({"msg" : "Group created", "group_id" : group.id})