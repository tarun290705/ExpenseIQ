from models.expense import Expense, Split
from models.settlement import Settlement
from collections import defaultdict

def calculate_balances(group_id):
    balances = {}

    splits = Split.query.join(Expense).filter(Expense.group_id==group_id).all()
    for s in splits:
        balances[s.user_id] = balances.get(s.user_id, 0) - s.amount

    expenses = Expense.query.filter_by(group_id=group_id).all()
    for e in expenses:
        balances[e.paid_by] = balances.get(e.paid_by, 0) + e.amount

    settlements = Settlement.query.filter_by(group_id=group_id).all()
    for s in settlements:
        balances[s.paid_by] = balances.get(s.paid_by, 0) - s.amount
        balances[s.received_by] = balances.get(s.received_by, 0) + s.amount

    return balances