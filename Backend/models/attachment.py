from extensions import db

class Attachment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expense_id = db.column(db.Integer, db.ForeignKey("expense.id"), nullable=False)
    filename = db.column(db.String(200), nullable=False)
    filepath = db.Column(db.String(300), nullable=False)