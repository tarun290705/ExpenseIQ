from flask import Blueprint, request, jsonify
from models.group import Group, GroupMember
from extensions import db
from utils.decorators import token_required

group_bp = Blueprint("group", __name__)

@group_bp.route("/create", methods=["POST"])
@token_required
def create_group(current_user):
    data = request.get_json()
    group = Group(name=data["name"])
    db.session.add(group)
    db.session.commit()

    gm = GroupMember(user_id=current_user.id, group_id=group.id, role="admin")
    db.session.add(gm)
    db.session.commit()
    return jsonify({"msg" : "Group created", "group_id" : group.id})

@group_bp.route("/<int:group_id>/join", methods=["POST"])
@token_required
def join_group(current_user, group_id):
    gm = GroupMember(user_id=current_user.id, group_id=group_id, role="member")
    db.seesion.add(gm)
    db.session.commit()
    return jsonify({"msg" : "Joined group successfully"})

@group_bp.route("/<int:group_id>/members", methods=["GET"])
@token_required
def group_members(current_user, group_id):
    members = GroupMember.query.filter_by(group_id=group_id).all()
    return jsonify([{"user_id" : m.user_id, "role" : m.role} for m in members])