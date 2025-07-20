from extensions import db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    members = db.realtionship("GroupMember", backref="group", lazy=True)
    expenses = db.relationship("Expense", backref="group", lazy=True)

class GroupMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    group_id = db.column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    role = db.column(db.String(20), default="member")