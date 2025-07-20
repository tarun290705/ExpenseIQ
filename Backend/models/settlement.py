from extensions import db

class settlement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    paid_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    received_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.column(db.DateTime, server_deafult=db.func.now())