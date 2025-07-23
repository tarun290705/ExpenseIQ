from models.expense import Expense, Split
from extensions import db

def add_expense(title, amount, paid_by, group_id, splits):
    expense = Expense(title=title, amount=amount, paid_by=paid_by, group_id=group_id)
    db.session.add(expense)
    db.session.commit()

    for split in splits:
        s = Split(expense_id=expense.id, user_id=split["user_id"], amount=split["amount"])
        db.session.add(s)
    db.session.commit()
    return expense

def get_group_expense(group_id):
    return Expense.query.filter_by(group_id=group_id).all()