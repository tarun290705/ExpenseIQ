from models.group import GroupMember
from extensions import db

def assign_role(user_id, group_id, role):
    member = GroupMember.query.filter_by(user_id=user_id, group_id=group_id).first()
    if member:
        member.role = role
        db.session.commit()
        return member
    return None