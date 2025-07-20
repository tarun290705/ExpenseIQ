from extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    groups = db.relationship("GroupMember", backref="user", lazy=True)
    expenses_paid = db.realtionship("Expense", backref="payer", lazy=True)
    splits = db.relationship("split", backref="user", lazy=True)
    settlement_sent = db.relationship("Settlement", backref="payer", foreign_keys="Settlement.paid_by", lazy=True)
    settlement_received = db.relationship("Settlement", backref="receiver", foreign_keys="Settlement.received_by", lazy=True)