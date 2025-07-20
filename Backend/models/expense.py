from extensions import db

class Expense(db.Model):
    id = db.column(db.Integer, primary_key=True)
    group_id = db.column(db.Integer, db.ForeignKey("group.id"), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    paid_by = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    timestamp = db.column(db.DateTime, server_deafult=db.func.now())

    splits = db.relationship("split", backref="expense", lazy=True)
    attachements = db.relationship("Attachment", backref="expense", lazy=True)

class Split(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expense_id = db.Column(db.Integer, db.ForeignKey("expense.id"), nullable=False)
    user_id = db.Column(db.Integre, db.ForeignKey("user.id"), nullable=False)
    amount = db.Column(db.Float, nullable=False)